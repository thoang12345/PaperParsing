# Paper Parsing RAG Pipeline

This project explores the development of a Retrieval-Augmented Generation (RAG) document ingestion pipeline for technical papers. The primary objective is to evaluate different document parsing strategies while building a modular system capable of converting unstructured documents into high-quality, searchable knowledge bases.

The project is currently in active development and has evolved through two major versions.

---

# v0.1 – Docling-Based Pipeline

The initial implementation focused on demonstrating a complete end-to-end RAG ingestion workflow using **Docling** as the sole document parser.

Documents were parsed into Markdown, chunked using a hybrid Markdown and token-based strategy, summarized with a local language model to generate contextual metadata, and stored in **ChromaDB** for semantic retrieval. The pipeline successfully demonstrated automated document ingestion, metadata generation, vector database integration, and basic retrieval capabilities.

While functional, the architecture tightly coupled document conversion, chunking, summarization, and database insertion into a single workflow. This made experimentation with different parsers and chunking strategies increasingly difficult as the project grew.

---

# v0.2 – Modular Multi-Parser Pipeline *(Current)*

The current version redesigns the project around a modular architecture that separates document classification, parsing, chunking, vector storage, and retrieval into independent components.

Rather than relying exclusively on Docling, v0.2 supports multiple parsing backends:

* **Docling** for general-purpose document parsing and native document structure extraction.
* **Marker 2** for high-fidelity PDF parsing, particularly for scientific papers, multi-column layouts, tables, mathematical content, and image extraction.

Incoming documents are first classified before being routed to the appropriate parser. Both parsers produce standardized outputs that feed into a common downstream pipeline, allowing different parsing strategies to be evaluated without modifying later stages of the system.

Current development is focused on:

* Completing parser integration
* Finalizing parser-independent chunking
* Standardizing metadata across parsing backends
* Integrating ChromaDB ingestion
* Evaluating retrieval performance across different parsing strategies

---

# Current Status

The v0.2 pipeline is a **work in progress**. While the overall architecture has been established and both parsing backends are operational, several components—including chunking, embedding generation, database ingestion, and retrieval evaluation—are still being actively developed and refined.

The long-term objective is to create a flexible, modular RAG pipeline capable of processing a wide range of technical documents while allowing individual components—such as parsers, chunkers, embedding models, and vector databases—to be swapped or improved independently.
