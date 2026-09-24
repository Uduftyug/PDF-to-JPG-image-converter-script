from __future__ import annotations

import argparse
from pathlib import Path

import fitz

PDF_DIR = Path(__file__).with_name("results")
JPG_DIR = PDF_DIR / "jpg"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert result PDFs to JPG images."
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="Image resolution in DPI (default: 150).",
    )
    return parser.parse_args()


def convert_pdf(pdf_path: Path, output_dir: Path, dpi: int) -> int:
    document = fitz.open(pdf_path)
    try:
        scale = dpi / 72
        matrix = fitz.Matrix(scale, scale)
        converted_pages = 0
        for page_number, page in enumerate(document, 1):
            image_path = output_dir / f"{pdf_path.stem}_{page_number}.jpg"
            if image_path.exists():
                print(f"Already exists, skipping {image_path.name}")
                continue

            pixmap = page.get_pixmap(matrix=matrix, alpha=False)
            pixmap.save(image_path)
            converted_pages += 1
            print(f"Saved {image_path}")
        return converted_pages
    finally:
        document.close()


def main() -> None:
    args = parse_args()
    if args.dpi < 36:
        raise SystemExit("--dpi must be at least 36")

    if not PDF_DIR.exists():
        raise SystemExit(f"PDF folder does not exist: {PDF_DIR}")

    pdf_files = sorted(PDF_DIR.glob("*.pdf"))
    if not pdf_files:
        raise SystemExit(f"No PDF files found in {PDF_DIR}")

    JPG_DIR.mkdir(exist_ok=True)
    converted_pages = 0
    for pdf_path in pdf_files:
        print(f"\nConverting {pdf_path.name}")
        converted_pages += convert_pdf(pdf_path, JPG_DIR, args.dpi)

    print(f"\nDone. Converted {converted_pages} page(s) into {JPG_DIR}")


if __name__ == "__main__":
    main()
