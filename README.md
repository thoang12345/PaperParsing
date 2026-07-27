# Current RAG Pipeline (Work in Progress)

> **Project Status:** 🚧 **Work in Progress**
>
> This project is an actively developed Retrieval-Augmented Generation (RAG) pipeline. The overall architecture is in place, but several stages are still being refined, optimized, and integrated. Features, parser configurations, chunking strategies, and retrieval quality should be considered experimental until the pipeline is complete.

## Overview

The goal of this project is to build a modular document-ingestion pipeline capable of processing a wide variety of technical documents into a searchable vector database.

The pipeline is designed around interchangeable parsing backends, allowing different document types to be processed using the parser best suited for the job. Current development focuses on integrating both **Docling** and **Marker 2** into a common workflow while maintaining a unified downstream chunking and retrieval process.

Current execution flow:

```text
Input/
   │
   ▼
GPU / System Initialization
   │
   ▼
Initialize Docling Chunker
   │
   ▼
Build Project Paths
   │
   ▼
Create ChromaDB Client
   │
   ▼
Classify Input Documents
   │
   ├── PDF Classification
   └── General File Classification
   │
   ▼
Display Parsing Plan
   │
   ▼
Create / Open Chroma Collection
   │
   ▼
(Optional) Query Existing Collection
   │
   ▼
Document Conversion
      ├── Marker 2
      └── Docling
```

## Current Components

### Document Classification

Every document is analyzed before parsing.

The classifier determines:

* Document type
* Appropriate parser
* Parsing profile
* Output location

This allows the pipeline to automatically route documents to the most suitable parsing backend.

---

### Parsing Backends

#### Marker 2

Marker is currently used for high-fidelity PDF extraction, particularly for:

* Scientific papers
* Technical reports
* Multi-column layouts
* Tables
* Mathematical content

Current features include:

* Native SDK integration (no CLI subprocesses)
* Optional Ollama-powered LLM processors
* Markdown export
* JSON export
* Embedded image extraction

---

#### Docling

Docling serves as the general-purpose document parser.

Current focus includes:

* General PDF parsing
* Office document support
* Native document chunking
* Rich document structure extraction

The long-term goal is for Docling to become the primary ingestion engine, with Marker acting as a specialized parser for complex PDFs.

---

### Chunking *(Currently Under Development)*

Chunking has been partially implemented but is not yet integrated into the main execution flow.

Current work includes:

* Docling HybridChunker
* Token-aware chunk sizing
* Metadata generation
* Parser-independent chunk normalization

Future work includes:

* Context-aware chunk generation
* Parser output normalization
* Chunk quality evaluation
* Retrieval benchmarking

---

### ChromaDB Integration *(Currently Under Development)*

A ChromaDB client is initialized at startup.

Current capabilities include:

* Creating collections
* Opening existing collections
* Basic query interface

Automatic ingestion of parsed chunks into ChromaDB is currently disabled while the chunking pipeline is being finalized.

---

### Query System

A basic query interface is available for interacting with existing Chroma collections.

Future work will expand this into a full retrieval pipeline supporting:

* Similarity search
* Metadata filtering
* Source citations
* Multi-document retrieval

---

## Current Development Priorities

Current work is focused on completing the ingestion pipeline in the following order:

1. Finish parser integration
2. Finalize chunk generation
3. Normalize metadata between parsers
4. Integrate automatic ChromaDB ingestion
5. Evaluate retrieval quality
6. Add answer generation using retrieved context

---

## Design Philosophy

The project is intentionally modular.

Rather than treating parsing, chunking, embedding, and retrieval as a single process, each stage is implemented as an independent component.

This allows:

* Multiple parsing backends
* Independent parser benchmarking
* Configurable chunking strategies
* Future embedding model replacement
* Vector database portability

The long-term objective is a flexible RAG ingestion pipeline that can reliably process technical documents while remaining easy to extend as new parsers, embedding models, and retrieval techniques become available.

---