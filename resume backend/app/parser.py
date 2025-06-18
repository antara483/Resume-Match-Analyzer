# import os
# import fitz  # PyMuPDF
# import textract
# from PIL import Image
# import pytesseract
# import io



# def extract_text_from_resume(file_path):
#     ext = os.path.splitext(file_path)[1].lower()

#     try:
#         if ext == '.pdf':
#             return extract_text_from_pdf_with_ocr(file_path)
#         elif ext == '.docx':
#             return textract.process(file_path).decode("utf-8")
#         else:
#             print(f"Unsupported file type: {ext}")
#             return ""
#     except Exception as e:
#         print(f"Error parsing resume: {e}")
#         return ""
# # below
# # def extract_text_from_pdf_with_ocr(filepath):
# #     text = ""
# #     try:
# #         with fitz.open(filepath) as doc:
# #             for i, page in enumerate(doc):
# #                 page_text = page.get_text()
# #                 if page_text.strip():
# #                     text += page_text
# #                 else:
# #                     # OCR fallback
# #                     pix = page.get_pixmap()
# #                     img = Image.open(io.BytesIO(pix.tobytes()))
# #                     ocr_text = pytesseract.image_to_string(img)
# #                     print(f"OCR used on page {i+1}")
# #                     text += ocr_text
# #         return text
# #     except Exception as e:
# #         print(f"Error reading PDF with OCR: {e}")
# #         return ""
# # below

# # deep
# # def extract_text_from_pdf_with_ocr(filepath):
# #     text = ""
# #     try:
# #         with fitz.open(filepath) as doc:
# #             for page in doc:
# #                 # Try text extraction first
# #                 page_text = page.get_text("text")
# #                 if page_text.strip():
# #                     text += page_text + "\n"
# #                 else:
# #                     # OCR fallback with better preprocessing
# #                     pix = page.get_pixmap(dpi=300)  # Higher DPI for better OCR
# #                     img = Image.open(io.BytesIO(pix.tobytes()))
# #                     # Enhance image for OCR
# #                     img = img.convert('L')  # Grayscale
# #                     ocr_text = pytesseract.image_to_string(img, config='--psm 6')
# #                     text += ocr_text + "\n"
# #         return text.strip()
# #     except Exception as e:
# #         print(f"Error reading PDF with OCR: {e}")
# #         return ""
# def extract_text_from_pdf_with_ocr(filepath):
#     text = ""
#     try:
#         with fitz.open(filepath) as doc:
#             for page in doc:
#                 # First try regular text extraction
#                 page_text = page.get_text("text", flags=fitz.TEXT_PRESERVE_WHITESPACE)
#                 if len(page_text.strip()) > 50:  # Only use if substantial text found
#                     text += page_text + "\n"
#                 else:
#                     # Enhanced OCR processing
#                     pix = page.get_pixmap(dpi=300)
#                     img = Image.open(io.BytesIO(pix.tobytes()))
#                     # Preprocess image for better OCR
#                     img = img.convert('L')  # Grayscale
#                     img = img.point(lambda x: 0 if x < 140 else 255)  # Thresholding
#                     ocr_text = pytesseract.image_to_string(img, config='--psm 6 --oem 3')
#                     text += ocr_text + "\n"
#         return text.strip()
#     except Exception as e:
#         print(f"Error processing PDF: {e}")
#         return ""
# # deep
# import os
# import fitz  # PyMuPDF
# import textract
# from PIL import Image
# import pytesseract
# import io

# def extract_text_from_resume(file_path):
#     ext = os.path.splitext(file_path)[1].lower()

#     try:
#         if ext == '.pdf':
#             return extract_text_from_pdf_with_ocr(file_path)
#         elif ext == '.docx':
#             return textract.process(file_path).decode("utf-8")
#         else:
#             print(f"Unsupported file type: {ext}")
#             return ""
#     except Exception as e:
#         print(f"Error parsing resume: {e}")
#         return ""

# def extract_text_from_pdf_with_ocr(filepath):
#     text = ""
#     try:
#         with fitz.open(filepath) as doc:
#             for page in doc:
#                 page_text = page.get_text("text", flags=fitz.TEXT_PRESERVE_WHITESPACE)
#                 if len(page_text.strip()) > 50:
#                     text += page_text + "\n"
#                 else:
#                     pix = page.get_pixmap(dpi=300)
#                     img = Image.open(io.BytesIO(pix.tobytes()))
#                     img = img.convert('L')  # Grayscale
#                     img = img.point(lambda x: 0 if x < 140 else 255)  # Thresholding
#                     ocr_text = pytesseract.image_to_string(img, config='--psm 6 --oem 3')
#                     text += ocr_text + "\n"
#         return text.strip()
#     except Exception as e:
#         print(f"Error processing PDF: {e}")
#         return ""

import os
import fitz  # PyMuPDF
import textract
from PIL import Image
import pytesseract
import io
import logging
import unicodedata

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def normalize_text(text):
    """Normalize Unicode characters and clean up text"""
    if not text:
        return ""
    
    # Normalize Unicode and replace problematic characters
    text = unicodedata.normalize('NFKC', text)
    replacements = {
        '→': '->', '–': '-', '—': '-', '‘': "'", '’': "'",
        '“': '"', '”': '"', '…': '...', '•': '*', '�': ''
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    
    return text.strip()

def extract_text_from_resume(file_path):
    """Extract text from various resume file formats with robust error handling"""
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return ""

    ext = os.path.splitext(file_path)[1].lower()
    
    try:
        if ext == '.pdf':
            return extract_text_from_pdf_with_ocr(file_path)
        elif ext == '.docx':
            text = textract.process(file_path).decode('utf-8', errors='replace')
            return normalize_text(text)
        elif ext in ('.txt', '.rtf'):
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                return normalize_text(f.read())
        else:
            logger.warning(f"Unsupported file type: {ext}")
            return ""
    except Exception as e:
        logger.error(f"Error parsing resume {file_path}: {str(e)}", exc_info=True)
        return ""

# def extract_text_from_pdf_with_ocr(filepath):
#     """Extract text from PDF using PyMuPDF with fallback to OCR"""
#     text = ""
#     try:
#         with fitz.open(filepath) as doc:
#             for page in doc:
#                 # First try to extract regular text
#                 page_text = page.get_text("text", flags=fitz.TEXT_PRESERVE_WHITESPACE)
#                 page_text = normalize_text(page_text)
                
#                 # If we got less than 50 characters, try OCR
#                 if len(page_text.strip()) < 50:
#                     try:
#                         pix = page.get_pixmap(dpi=300)
#                         img = Image.open(io.BytesIO(pix.tobytes()))
                        
#                         # Preprocess image for better OCR
#                         img = img.convert('L')  # Grayscale
#                         img = img.point(lambda x: 0 if x < 140 else 255)  # Thresholding
                        
#                         # Configure Tesseract for resumes
#                         ocr_text = pytesseract.image_to_string(
#                             img, 
#                             config='--psm 6 --oem 3 -c preserve_interword_spaces=1'
#                         )
#                         page_text = normalize_text(ocr_text)
                        
#                     except Exception as ocr_error:
#                         logger.warning(f"OCR failed on page {page.number}: {str(ocr_error)}")
#                         continue
                
#                 if page_text.strip():
#                     text += page_text + "\n\n"  # Add extra

def extract_text_from_pdf_with_ocr(filepath):
    """Extract text from PDF using PyMuPDF with fallback to OCR"""
    text = ""
    try:
        with fitz.open(filepath) as doc:
            for page in doc:
                try:
                    # First try to extract regular text
                    page_text = page.get_text("text", flags=fitz.TEXT_PRESERVE_WHITESPACE)
                    page_text = normalize_text(page_text)
                    
                    # If we got less than 50 characters, try OCR
                    if len(page_text.strip()) < 50:
                        try:
                            pix = page.get_pixmap(dpi=300)
                            img = Image.open(io.BytesIO(pix.tobytes()))
                            
                            # Preprocess image for better OCR
                            img = img.convert('L')  # Grayscale
                            img = img.point(lambda x: 0 if x < 140 else 255)  # Thresholding
                            
                            # Configure Tesseract for resumes
                            ocr_text = pytesseract.image_to_string(
                                img, 
                                config='--psm 6 --oem 3 -c preserve_interword_spaces=1'
                            )
                            page_text = normalize_text(ocr_text)
                            
                        except Exception as ocr_error:
                            logger.warning(f"OCR failed on page {page.number}: {str(ocr_error)}")
                            continue
                    
                    if page_text.strip():
                        text += page_text + "\n\n"  # Add extra newline between pages
                        
                except Exception as page_error:
                    logger.warning(f"Error processing page {page.number}: {str(page_error)}")
                    continue
                    
        return text.strip()
    
    except Exception as e:
        logger.error(f"PDF processing failed for {filepath}: {str(e)}", exc_info=True)
        return ""