from __future__ import annotations
import re
from typing import Any, Literal, TypedDict
from pathlib import Path
import fitz
import random
from Functions import functions as fun

def classifyPDFs(path : Path) -> dict[str : str]:
        pdfs, not_pdfs = fun.separatePDFs(path)
        pageData = extractPageData(path, pdfs)
        classifications = classify(pageData)

        return classifications   

def classify(pageDataPDFs: list[dict[str, str | list[dict[str, int]]]]) -> list[dict[str, str]]:
    results = []

    for pdf in pageDataPDFs:
        fileName = pdf["file"]
        pages = pdf["pages"]
        text = pdf["text"]

        features = build_content_features(text=text, pages=pages)
        textType = classifyTextType(features)
        contentDetails = classify_content_type_details(features)
        
        contentType = contentDetails["content_type"]

        results.append({
            "file": fileName,
            "text_type": textType,
            "content_type": contentType,
        })

    return results

def summarizePDFPages(pages: list[dict[str, int]]) -> dict[str, int]:
    totalWords = 0
    totalImages = 0
    pageCount = len(pages)
    maxWordsOnPage = 0
    imageHeavyPages = 0
    textHeavyPages = 0

    for page in pages:
        words = page["words"]
        images = page["images"]

        totalWords += words
        totalImages += images

        if words > maxWordsOnPage:
            maxWordsOnPage = words

        # page has a meaningful amount of text
        if words >= 50:
            textHeavyPages += 1

        # page has images on it
        if images > 0:
            imageHeavyPages += 1

    return {
        "total_words_from_pages": totalWords,
        "total_images": totalImages,
        "page_count": pageCount,
        "max_words_on_page": maxWordsOnPage,
        "image_heavy_pages": imageHeavyPages,
        "text_heavy_pages": textHeavyPages,
    }
def classifyTextType(features: dict[str, int]) -> str:
    totalWords = features["total_words_from_pages"]
    totalImages = features["total_images"]
    pageCount = features["page_count"]
    imageHeavyPages = features["image_heavy_pages"]
    textHeavyPages = features["word_heavy_pages"]

    if pageCount == 0:
        return "unknown"

    averageWordsPerPage = totalWords / pageCount
    imagePageRatio = imageHeavyPages / pageCount
    textPageRatio = textHeavyPages / pageCount

    # scanned / image-first
    if averageWordsPerPage < 20 and imagePageRatio > 0.6:
        return "scannedPDF"

    # mixed should come before native
    if averageWordsPerPage >= 20 and textPageRatio > 0.4 and imagePageRatio > 0.25:
        return "mixedPDF"

    # OCRed scan: text exists, but images are still very common
    if averageWordsPerPage >= 20 and imagePageRatio > 0.6:
        return "OCRedPDF"

    # native text PDF
    if averageWordsPerPage > 150 and imagePageRatio < 0.25:
        return "nativePDF"

    return "unknown"

def extractPageData(path: Path, pdfs: list[str]) -> list[dict[str, str | list[dict[str, int]]]]:

    specificPages = pageList(path, pdfs)
    pageData = []

    for i, pdf in enumerate(pdfs):

        pages = []
        combined_text = ""

        with fitz.open(path / pdf) as doc:

            for pageNum in specificPages[i]:

                page = doc[pageNum]

                page_text = page.get_text()

                pages.append({
                    "page_number": page.number + 1,
                    "words": len(page.get_text("words")),
                    "images": len(page.get_images(full=True))
                })

                combined_text += (
                    f"\n\n--- PAGE {page.number + 1} ---\n\n"
                    + page_text
                )

        pageData.append({
            "file": pdf,
            "pages": pages,
            "text": combined_text
        })

    return pageData        
           
def countPages(path : Path, pdfs : list[str]) -> list[int]:
        pageNumber = []
        for pdf in (pdfs):
                with fitz.open(path / pdf) as doc:
                        pageNumber.append(doc.page_count)
        return pageNumber                        
                
def pageList(path : Path, pdfs : list[str]) -> list[list[int]]:
        listPageNumbers = countPages(path, pdfs)
        specificPages = []
        for pageNumber in listPageNumbers:
                middle = (pageNumber + 1) // 2
                if pageNumber < 4:
                        specificPages.append([0, -1, middle])
                elif pageNumber > 5 and pageNumber < 11:
                        specificPages.append([0, 1, -1, -2, middle])
                else:
                        specificPages.append([0, 1, -1, -2, middle, middle - 1, random.randint(2, middle - 2), random.randint(2, middle - 2), random. randint(middle + 1, pageNumber - 3), random. randint(middle + 1, pageNumber - 3)])
        return specificPages 

ContentType = Literal[
    "scientific",
    "business_report",
    "legal",
    "financial",
    "slide_export",
    "form",
    "generic",
]

class PageData(TypedDict):
    page_number: int
    words: int
    images: int


class PDFRecord(TypedDict):
    file: str
    pages: list[PageData]


# ----------------------------
# Keyword groups
# ----------------------------

SCIENTIFIC_KEYWORDS = [
    "abstract",
    "introduction",
    "method",
    "methods",
    "methodology",
    "results",
    "discussion",
    "conclusion",
    "experiment",
    "dataset",
    "hypothesis",
    "analysis",
    "evaluation",
    "baseline",
    "accuracy",
    "statistical",
    "simulation",
    "model",
    "measurement",
    "references",
    "bibliography",
]

BUSINESS_KEYWORDS = [
    "executive summary",
    "overview",
    "strategy",
    "market",
    "operations",
    "recommendation",
    "recommendations",
    "stakeholder",
    "performance",
    "growth",
    "roadmap",
    "initiative",
    "business",
    "customer",
    "management",
]

LEGAL_KEYWORDS = [
    "agreement",
    "contract",
    "party",
    "parties",
    "liability",
    "jurisdiction",
    "governing law",
    "clause",
    "warranty",
    "indemnification",
    "terms",
    "conditions",
    "hereby",
    "whereas",
    "pursuant",
    "shall",
]

FINANCIAL_KEYWORDS = [
    "revenue",
    "profit",
    "loss",
    "income",
    "expense",
    "expenses",
    "assets",
    "liabilities",
    "equity",
    "cash flow",
    "balance sheet",
    "fiscal year",
    "quarter",
    "earnings",
    "ebitda",
    "operating income",
    "net income",
]

FORM_KEYWORDS = [
    "name",
    "date",
    "address",
    "phone",
    "email",
    "signature",
    "applicant",
    "account number",
    "yes",
    "no",
]


# ----------------------------
# Regex patterns
# ----------------------------

DOI_RE = re.compile(
    r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b",
    re.IGNORECASE,
)

BRACKET_CITATION_RE = re.compile(
    r"\[(?:\d{1,3}(?:\s*[-,]\s*\d{1,3})*)\]"
)

AUTHOR_YEAR_CITATION_RE = re.compile(
    r"\([A-Z][A-Za-z\-]+(?:\s+et\s+al\.)?(?:,\s*|\s+)\d{4}[a-z]?\)",
    re.IGNORECASE,
)

FIGURE_CAPTION_RE = re.compile(
    r"(?im)^\s*(?:fig\.|figure)\s+\d+"
)

TABLE_CAPTION_RE = re.compile(
    r"(?im)^\s*table\s+\d+"
)

EQUATION_RE = re.compile(
    r"(?m)(?:"
    r"\b[a-zA-Z]\s*=\s*[^,\n]{2,}"
    r"|\\begin\{equation\}"
    r"|\\frac"
    r"|\\sum"
    r"|\\int"
    r"|[∑∫√≤≥≈≠±×÷αβγδλμσθΩ]"
    r")"
)

CURRENCY_RE = re.compile(
    r"[$€£¥]\s?\d|\b\d+(?:\.\d+)?\s?(?:USD|EUR|GBP|JPY)\b",
    re.IGNORECASE,
)

NUMBER_RE = re.compile(
    r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?%?\b"
)

LEGAL_SECTION_RE = re.compile(
    r"(?im)^\s*(?:section|article|clause)\s+\d+"
)

SIGNATURE_RE = re.compile(
    r"(?im)\bsignature\b|_{5,}\s*(?:date|name)?"
)

CHECKBOX_RE = re.compile(
    r"☐|☑|□|■|\[\s*[xX]?\s*\]"
)

FORM_LINE_RE = re.compile(
    r"(?im)\b(name|date|address|phone|email|signature|applicant|account number)\b\s*[:_]"
)

BULLET_RE = re.compile(
    r"(?m)^\s*(?:[-*•]|[0-9]+[.)])\s+"
)


# ----------------------------
# Helper functions
# ----------------------------

def count_terms(text: str, terms: list[str]) -> int:
    """
    Count how often a list of terms appears in text.
    Handles both single-word and multi-word phrases.
    """
    text = text.lower()
    total = 0

    for term in terms:
        escaped = re.escape(term.lower()).replace(r"\ ", r"\s+")
        pattern = rf"\b{escaped}\b"
        total += len(re.findall(pattern, text))

    return total


def has_heading(text: str, heading: str) -> bool:
    """
    Detect a heading-like line.

    Examples it catches:
        Abstract
        1 Introduction
        2.1 Methods
        References:
    """
    pattern = rf"(?im)^\s*(?:\d+(?:\.\d+)*\s+)?{re.escape(heading)}\b\s*[:\-–]?"
    return bool(re.search(pattern, text))


def points(value: int | float, medium: int | float, high: int | float) -> int:
    """
    Convert a count into simple score points.
    """
    if value >= high:
        return 2
    if value >= medium:
        return 1
    return 0


# ----------------------------
# Feature extraction
# ----------------------------

def build_content_features(
    text: str = "",
    pages: list[PageData] | None = None,
) -> dict[str, Any]:
    """
    Builds a feature dictionary that the content classifier can use.

    This function does NOT open the PDF.
    It only uses:
        - extracted text you pass in
        - page metadata you pass in
    """
    pages = pages or []

    page_count = len(pages)

    total_words_from_pages = sum(page.get("words", 0) for page in pages)
    total_images = sum(page.get("images", 0) for page in pages)

    pages_with_text = sum(1 for page in pages if page.get("words", 0) > 50)
    pages_with_images = sum(1 for page in pages if page.get("images", 0) > 0)

    avg_words_per_page = (
        total_words_from_pages / page_count
        if page_count > 0
        else 0
    )

    image_ratio = (
        pages_with_images / page_count
        if page_count > 0
        else 0
    )

    text_word_count = len(re.findall(r"\b[\w'-]+\b", text))

    citation_count = (
        len(BRACKET_CITATION_RE.findall(text))
        + len(AUTHOR_YEAR_CITATION_RE.findall(text))
    )

    max_words_on_page = max(
    (page["words"] for page in pages),
    default=0   
    )

    word_heavy_pages = sum(
    1 for page in pages
    if page["words"] > 150
    )

    image_heavy_pages = sum(
        1 for page in pages
        if page["images"] > 0
    )

    features = {
        "text": text,
        "page_count": page_count,
        "total_words_from_pages": total_words_from_pages,
        "text_word_count": text_word_count,
        "total_images": total_images,
        "avg_words_per_page": avg_words_per_page,
        "pages_with_text": pages_with_text,
        "pages_with_images": pages_with_images,
        "image_ratio": image_ratio,
        "max_words_on_page": max_words_on_page,
        "image_heavy_pages": image_heavy_pages,
        "word_heavy_pages": word_heavy_pages,

        # Scientific signals
        "has_abstract": has_heading(text, "abstract"),
        "has_introduction": has_heading(text, "introduction"),
        "has_methods": has_heading(text, "methods") or has_heading(text, "methodology"),
        "has_results": has_heading(text, "results"),
        "has_discussion": has_heading(text, "discussion"),
        "has_references": has_heading(text, "references") or has_heading(text, "bibliography"),
        "citation_count": citation_count,
        "doi_count": len(DOI_RE.findall(text)),
        "equation_count": len(EQUATION_RE.findall(text)),
        "figure_caption_count": len(FIGURE_CAPTION_RE.findall(text)),
        "table_caption_count": len(TABLE_CAPTION_RE.findall(text)),
        "scientific_keyword_hits": count_terms(text, SCIENTIFIC_KEYWORDS),

        # Business signals
        "business_keyword_hits": count_terms(text, BUSINESS_KEYWORDS),
        "has_executive_summary": has_heading(text, "executive summary"),
        "has_recommendations": has_heading(text, "recommendations"),

        # Legal signals
        "legal_keyword_hits": count_terms(text, LEGAL_KEYWORDS),
        "legal_section_count": len(LEGAL_SECTION_RE.findall(text)),
        "signature_count": len(SIGNATURE_RE.findall(text)),

        # Financial signals
        "financial_keyword_hits": count_terms(text, FINANCIAL_KEYWORDS),
        "currency_count": len(CURRENCY_RE.findall(text)),
        "number_count": len(NUMBER_RE.findall(text)),
        "has_balance_sheet": "balance sheet" in text.lower(),
        "has_income_statement": "income statement" in text.lower(),
        "has_cash_flow": "cash flow" in text.lower(),

        # Slide signals
        "bullet_count": len(BULLET_RE.findall(text)),

        # Form signals
        "form_keyword_hits": count_terms(text, FORM_KEYWORDS),
        "checkbox_count": len(CHECKBOX_RE.findall(text)),
        "form_line_count": len(FORM_LINE_RE.findall(text)),
    }

    return features


# ----------------------------
# Individual scoring functions
# ----------------------------

def score_scientific(features: dict[str, Any]) -> int:
    score = 0

    if features["has_abstract"]:
        score += 3

    if features["has_introduction"]:
        score += 1

    if features["has_methods"]:
        score += 2

    if features["has_results"]:
        score += 2

    if features["has_discussion"]:
        score += 1

    if features["has_references"]:
        score += 3

    score += points(features["citation_count"], medium=2, high=8)
    score += points(features["doi_count"], medium=1, high=2)
    score += points(features["equation_count"], medium=1, high=5)
    score += points(features["figure_caption_count"], medium=2, high=5)
    score += points(features["table_caption_count"], medium=1, high=4)
    score += points(features["scientific_keyword_hits"], medium=5, high=15)

    return score


def score_business_report(features: dict[str, Any]) -> int:
    score = 0

    if features["has_executive_summary"]:
        score += 3

    if features["has_recommendations"]:
        score += 2

    score += points(features["business_keyword_hits"], medium=5, high=15)

    # Business reports often have some charts/tables.
    if features["table_caption_count"] >= 2:
        score += 1

    if features["figure_caption_count"] >= 2:
        score += 1

    return score


def score_legal(features: dict[str, Any]) -> int:
    score = 0

    score += points(features["legal_keyword_hits"], medium=5, high=15)
    score += points(features["legal_section_count"], medium=2, high=6)
    score += points(features["signature_count"], medium=1, high=3)

    text = features["text"].lower()

    if "terms and conditions" in text:
        score += 3

    if "governing law" in text:
        score += 2

    if "indemnification" in text:
        score += 2

    return score


def score_financial(features: dict[str, Any]) -> int:
    score = 0

    score += points(features["financial_keyword_hits"], medium=5, high=15)
    score += points(features["currency_count"], medium=3, high=10)

    # Lots of numbers plus tables often means financial material.
    if features["number_count"] >= 50 and features["table_caption_count"] >= 1:
        score += 2

    if features["has_balance_sheet"]:
        score += 3

    if features["has_income_statement"]:
        score += 3

    if features["has_cash_flow"]:
        score += 3

    return score


def score_slide_export(features: dict[str, Any]) -> int:
    score = 0

    page_count = features["page_count"]
    avg_words = features["avg_words_per_page"]
    image_ratio = features["image_ratio"]
    bullet_count = features["bullet_count"]

    # Avoid calling a scanned PDF a slide deck just because it has low text.
    if page_count > 1 and avg_words > 20:
        if avg_words < 70:
            score += 2
        elif avg_words < 140:
            score += 1

    if bullet_count >= 10:
        score += 2
    elif bullet_count >= 4:
        score += 1

    if image_ratio >= 0.5 and avg_words > 20:
        score += 1

    return score


def score_form(features: dict[str, Any]) -> int:
    score = 0

    score += points(features["checkbox_count"], medium=1, high=4)
    score += points(features["form_line_count"], medium=3, high=8)
    score += points(features["form_keyword_hits"], medium=5, high=15)

    if features["signature_count"] >= 1:
        score += 2

    return score


# ----------------------------
# Final classifier
# ----------------------------

def content_type_scores(features: dict[str, Any]) -> dict[str, int]:
    return {
        "scientific": score_scientific(features),
        "business_report": score_business_report(features),
        "legal": score_legal(features),
        "financial": score_financial(features),
        "slide_export": score_slide_export(features),
        "form": score_form(features),
    }


def classify_content_type(
    features: dict[str, Any],
    minimum_score: int = 4,
    margin: int = 2,
) -> ContentType:
    """
    Classify the content type.

    minimum_score:
        The best label must score at least this much.

    margin:
        The best label must beat the second-best label by at least this much.
        This prevents uncertain documents from being over-classified.
    """
    scores = content_type_scores(features)

    ranked = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    best_label, best_score = ranked[0]
    second_best_score = ranked[1][1]

    if best_score < minimum_score:
        return "generic"

    if best_score - second_best_score < margin:
        return "generic"

    return best_label  # type: ignore[return-value]


def classify_content_type_details(
    features: dict[str, Any],
    minimum_score: int = 4,
    margin: int = 2,
) -> dict[str, Any]:
    """
    Same as classify_content_type, but also returns the score breakdown.
    Useful for debugging.
    """
    scores = content_type_scores(features)
    content_type = classify_content_type(
        features,
        minimum_score=minimum_score,
        margin=margin,
    )

    return {
        "content_type": content_type,
        "scores": scores,
    }

