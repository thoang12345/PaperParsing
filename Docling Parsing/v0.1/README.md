# RAG Pipeline (v0.1)

> **Version:** v0.1 (Archived)
>
> This version represents the first complete end-to-end implementation of the document ingestion pipeline. Its primary goal was to demonstrate that documents could be parsed, summarized, chunked, embedded, and stored in ChromaDB. While functional, the architecture tightly coupled parsing, chunking, summarization, and database insertion into a single workflow, making experimentation and maintenance increasingly difficult. This version has since been superseded by the modular v0.2 architecture.

## Overview

The v0.1 pipeline was built around **Docling** as the sole document parser. Documents were processed in batches, converted to Markdown, chunked using a hybrid Markdown/token-based strategy, summarized with a local language model, and immediately inserted into a ChromaDB collection.

The complete workflow was:

```text
Input Folder
      │
      ▼
Filter Previously Indexed Documents
      │
      ▼
Batch PDF Conversion (Docling)
      │
      ▼
Markdown Export
      │
      ▼
Markdown Post-Processing
      │
      ▼
Markdown Header Chunking
      │
      ▼
Recursive Token Chunking
      │
      ▼
LLM Context Summarization
      │
      ▼
Metadata Generation
      │
      ▼
ChromaDB Insertion
```

## Parsing

Document conversion was handled entirely by **Docling** using a configurable PDF pipeline. The parser supported OCR, table structure recognition, formula enrichment, page image generation, picture extraction, and optional picture descriptions. Pipeline behavior was controlled through a single configuration object that exposed settings such as OCR batch size, layout batch size, table batch size, OCR engine, and image scaling.

## Chunking

Rather than using Docling's native chunking pipeline, v0.1 exported each document as Markdown and performed a two-stage chunking process.

First, the Markdown was split according to document headers using a Markdown header splitter. Those header-based sections were then recursively divided into embedding-sized chunks using a token-aware recursive text splitter. This approach attempted to preserve document hierarchy while keeping chunks within a fixed token budget.

## Context Generation

Each chunk was sent to a locally hosted **Qwen 2.5 3B Instruct** model to generate a concise contextual summary. Previous and following chunks were included in the prompt to improve local context while instructing the model to summarize only the current chunk. The generated summary became part of the chunk metadata and was intended to improve semantic retrieval quality during vector search.

## Metadata

Every stored chunk included a standardized metadata record containing:

* Document headers
* Document name
* Starting page
* Chunk number
* LLM-generated contextual summary
* Token count

These metadata fields were written directly into ChromaDB alongside the document text to support filtering and retrieval.

## Vector Database

Embeddings and metadata were stored in a persistent **ChromaDB** collection using cosine similarity with a customized HNSW index configuration. Before processing, the pipeline checked whether a document had already been indexed, allowing the user to skip or overwrite existing records. A simple interactive query interface was also included for testing retrieval quality against the stored document collection.

## Limitations

Although v0.1 successfully demonstrated an end-to-end RAG ingestion workflow, several architectural limitations motivated the redesign that became v0.2.

* Parsing, chunking, summarization, and database insertion were tightly coupled into a single execution path.
* Only Docling was supported as a parsing backend.
* Chunking depended on exported Markdown rather than the parser's native document structure.
* Metadata generation and summarization were embedded directly into the ingestion pipeline instead of existing as reusable components.
* Parser configurations were centralized in a single configuration class, making it difficult to compare different parsing strategies or extend the system with additional backends.

These limitations ultimately led to the modular parser architecture introduced in v0.2, where document classification, parser selection, chunking, retrieval, and database operations are implemented as independent components.
