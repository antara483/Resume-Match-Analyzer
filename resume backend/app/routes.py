
# # deep
# from flask import Blueprint, render_template, request, flash
# from app import mysql
# import os
# from datetime import datetime
# from .parser import extract_text_from_resume
# from .matcher import ResumeMatcher  # Using the new class-based matcher

# main_routes = Blueprint('main_routes', __name__)

# # Configure upload folder
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @main_routes.route("/", methods=["GET", "POST"])
# def index():
#     results = []
#     debug_info = []  # Store debug information to display
    
#     if request.method == "POST":
#         # Check if files were uploaded
#         if 'resumes' not in request.files:
#             flash('No files selected', 'error')
#             return render_template("index.html", results=results)
        
#         uploaded_files = request.files.getlist("resumes")
#         if not uploaded_files or not uploaded_files[0].filename:
#             flash('No files selected', 'error')
#             return render_template("index.html", results=results)

#         # Initialize the matcher
#         matcher = ResumeMatcher()
        
#         try:
#             # Load all job descriptions from DB
#             cursor = mysql.connection.cursor()
#             cursor.execute("SELECT id, title, description FROM job_descriptions")
#             job_descriptions = cursor.fetchall()
#             cursor.close()

#             debug_info.append(f"Loaded {len(job_descriptions)} job descriptions from database")

#             for file in uploaded_files:
#                 if file.filename == '':
#                     continue

#                 # Save the file with timestamp to avoid overwrites
#                 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#                 safe_filename = f"{timestamp}_{file.filename.replace(' ', '_')}"
#                 filepath = os.path.join(UPLOAD_FOLDER, safe_filename)
#                 file.save(filepath)

#                 # Extract text from resume
#                 resume_text = extract_text_from_resume(filepath)
#                 debug_info.append(f"\nProcessing: {file.filename}")
#                 debug_info.append(f"Text length: {len(resume_text)} characters")
                
#                 if len(resume_text) < 100:
#                     debug_info.append("⚠️ Warning: Very short resume text - possible extraction issue")
#                     results.append({
#                         "filename": file.filename,
#                         "job_title": "Extraction Failed",
#                         "match": 0,
#                         "status": "Error",
#                         "debug": "Resume text too short (<100 chars)"
#                     })
#                     continue

#                 best_match = {"score": 0, "job_title": "No Match Found", "debug": []}
                
#                 # Compare against each job description
#                 for job_id, title, description in job_descriptions:
#                     if not description or len(description) < 50:
#                         continue  # Skip empty job descriptions
                    
#                     score = matcher.calculate_match_score(resume_text, description)
#                     best_match["debug"].append(f"Match with '{title[:30]}...': {score}%")
                    
#                     # Update best match if this score is higher
#                     if score > best_match["score"]:
#                         best_match.update({
#                             "score": score,
#                             "job_title": title,
#                             "best_description": description[:100] + "..." if len(description) > 100 else description
#                         })
                        
#                         # Early exit if we find a very good match
#                         if score >= 80:
#                             break

#                 # Determine status
#                 status = "Qualified" if best_match["score"] >= 65 else "Disqualified"
#                 if best_match["score"] >= 80:
#                     status = "Highly Qualified"
#                 elif best_match["score"] < 40:
#                     status = "Not Qualified"

#                 # Add to results
#                 results.append({
#                     "filename": file.filename,
#                     "job_title": best_match["job_title"],
#                     "match": best_match["score"],
#                     "status": status,
#                     "debug": "\n".join(best_match["debug"][:3])  # Show top 3 matches
#                 })

#         except Exception as e:
#             debug_info.append(f"⚠️ Error: {str(e)}")
#             flash(f'An error occurred: {str(e)}', 'error')

#     # Print debug info to console (remove in production)
#     for line in debug_info:
#         print(line)

#     return render_template("index.html", 
#                          results=results,
#                          debug_info=debug_info,
#                          show_debug=True)  # Set to False in production
# # deep

# from flask import Blueprint, request, jsonify
# from app import mysql
# import os
# from datetime import datetime
# from .parser import extract_text_from_resume
# from .matcher import ResumeMatcher

# main_routes = Blueprint('main_routes', __name__)

# @main.route("/", methods=["GET"])
# def home():
#     return {"message": "Resume Match Analyzer API is running"}, 200

# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @main_routes.route("/api/parse-resumes", methods=["POST"])
# def parse_resumes_api():
#     results = []
#     debug_info = []

#     if 'resumes' not in request.files:
#         return jsonify({"error": "No resumes file part in the request"}), 400

#     uploaded_files = request.files.getlist("resumes")
#     if not uploaded_files or not uploaded_files[0].filename:
#         return jsonify({"error": "No files selected"}), 400

#     matcher = ResumeMatcher()

#     try:
#         cursor = mysql.connection.cursor()
#         cursor.execute("SELECT id, title, description FROM job_descriptions")
#         job_descriptions = cursor.fetchall()
#         cursor.close()

#         debug_info.append(f"Loaded {len(job_descriptions)} job descriptions from database")

#         for file in uploaded_files:
#             if file.filename == '':
#                 continue

#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             safe_filename = f"{timestamp}_{file.filename.replace(' ', '_')}"
#             filepath = os.path.join(UPLOAD_FOLDER, safe_filename)
#             file.save(filepath)

#             resume_text = extract_text_from_resume(filepath)
#             debug_info.append(f"\nProcessing: {file.filename}")
#             debug_info.append(f"Text length: {len(resume_text)} characters")

#             if len(resume_text) < 100:
#                 debug_info.append("⚠️ Warning: Very short resume text - possible extraction issue")
#                 results.append({
#                     "filename": file.filename,
#                     "job_title": "Extraction Failed",
#                     "match": 0,
#                     "status": "Error",
#                     "debug": "Resume text too short (<100 chars)"
#                 })
#                 continue

#             best_match = {"score": 0, "job_title": "No Match Found", "debug": []}

#             for job_id, title, description in job_descriptions:
#                 if not description or len(description) < 50:
#                     continue

#                 score = matcher.calculate_match_score(resume_text, description)
#                 best_match["debug"].append(f"Match with '{title[:30]}...': {score}%")

#                 if score > best_match["score"]:
#                     best_match.update({
#                         "score": score,
#                         "job_title": title,
#                         "best_description": description[:100] + "..." if len(description) > 100 else description
#                     })

#                     if score >= 80:
#                         break

#             if best_match["score"] >= 80:
#                 status = "Highly Qualified"
#             elif best_match["score"] >= 50:
#                 status = "Qualified"
#             else:
#                 status = "Not Qualified"

#             results.append({
#                 "filename": file.filename,
#                 "job_title": best_match["job_title"],
#                 "match": best_match["score"],
#                 "status": status,
#                 "debug": best_match["debug"][:3]
#             })

#     except Exception as e:
#         return jsonify({"error": str(e), "debug_info": debug_info}), 500

#     return jsonify({
#         "results": results,
#         "debug_info": debug_info
#     })
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Blueprint, request, jsonify
from app import mysql
from PyPDF2 import PdfReader
import os
from datetime import datetime
from .parser import extract_text_from_resume
from .matcher import ResumeMatcher
from app.auth_utils import token_required

main_routes = Blueprint('main_routes', __name__)

@main_routes.route("/", methods=["GET"])
def home():
    return {"message": "Resume Match Analyzer API is running"}, 200

UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @main_routes.route("/api/parse-resumes", methods=["POST"])
# @token_required
# def parse_resumes_api():
#     results = []
#     debug_info = []

#     if 'resumes' not in request.files:
#         return jsonify({"error": "No resumes file part in the request"}), 400

#     uploaded_files = request.files.getlist("resumes")
#     if not uploaded_files or not uploaded_files[0].filename:
#         return jsonify({"error": "No files selected"}), 400

#     matcher = ResumeMatcher()

#     try:
#         cursor = mysql.connection.cursor()
#         cursor.execute("SELECT id, title, description FROM job_descriptions")
#         job_descriptions = cursor.fetchall()
#         cursor.close()

#         debug_info.append(f"Loaded {len(job_descriptions)} job descriptions from database")

#         for file in uploaded_files:
#             if file.filename == '':
#                 continue

#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             safe_filename = f"{timestamp}_{file.filename.replace(' ', '_')}"
#             filepath = os.path.join(UPLOAD_FOLDER, safe_filename)
#             file.save(filepath)

#             resume_text = extract_text_from_resume(filepath)
#             debug_info.append(f"\nProcessing: {file.filename}")
#             debug_info.append(f"Text length: {len(resume_text)} characters")

#             if len(resume_text) < 100:
#                 debug_info.append("⚠️ Warning: Very short resume text - possible extraction issue")
#                 results.append({
#                     "filename": file.filename,
#                     "job_title": "Extraction Failed",
#                     "match": 0,
#                     "status": "Error",
#                     "debug": "Resume text too short (<100 chars)"
#                 })
#                 continue

#             best_match = {"score": 0, "job_title": "No Match Found", "debug": []}

#             for job_id, title, description in job_descriptions:
#                 if not description or len(description) < 50:
#                     continue

#                 score = matcher.calculate_match_score(resume_text, description)
#                 best_match["debug"].append(f"Match with '{title[:30]}...': {score}%")

#                 if score > best_match["score"]:
#                     best_match.update({
#                         "score": score,
#                         "job_title": title,
#                         "best_description": description[:100] + "..." if len(description) > 100 else description
#                     })

#                     if score >= 80:
#                         break

#             if best_match["score"] >= 80:
#                 status = "Highly Qualified"
#             elif best_match["score"] >= 50:
#                 status = "Qualified"
#             else:
#                 status = "Not Qualified"

#             results.append({
#                 "filename": file.filename,
#                 "job_title": best_match["job_title"],
#                 "match": best_match["score"],
#                 "status": status,
#                 "debug": best_match["debug"][:3]
#             })

#     except Exception as e:
#         return jsonify({"error": str(e), "debug_info": debug_info}), 500

#     return jsonify({
#         "results": results,
#         "debug_info": debug_info
#     })



# Configure logging
# logging.basicConfig(filename='resume_parser.log', level=logging.INFO)
if not os.path.exists('logs'):
    os.mkdir('logs')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
    handlers=[
        RotatingFileHandler('logs/resume_parser.log', maxBytes=100000, backupCount=10),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Constants
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def extract_text_from_resume(filepath):
#     """Extract text from PDF with proper error handling and encoding"""
#     try:
#         text = ""
#         with open(filepath, 'rb') as f:
#             reader = PdfReader(f)
#             for page in reader.pages:
#                 page_text = page.extract_text()
#                 if page_text:
#                     text += page_text + "\n"
        
#         # Basic Unicode normalization
#         if text:
#             replacements = {
#                 "→": "->", "–": "-", "—": "-", "‘": "'", "’": "'",
#                 "“": '"', "”": '"', "…": "...", "•": "*", "�": ""
#             }
#             for orig, repl in replacements.items():
#                 text = text.replace(orig, repl)
        
#         return text.strip()
    
#     except Exception as e:
#         logger.error(f"Text extraction failed for {filepath}: {str(e)}")
#         return ""

def sanitize_debug_info(info_list):
    """Ensure debug info is safe for JSON serialization"""
    safe_list = []
    for entry in info_list:
        try:
            if not isinstance(entry, (str, bytes)):
                entry = str(entry)
            
            # Force UTF-8 encoding and replace problematic chars
            entry = (entry.encode('utf-8', errors='replace')
                      .decode('utf-8', errors='replace'))
            safe_list.append(entry.strip())
        except Exception as e:
            safe_list.append(f"[Sanitization error: {str(e)}]")
    return safe_list

# @main_routes.route("/api/parse-resumes", methods=["POST"])
# @token_required
# def parse_resumes_api(current_user):
#     """API endpoint for resume parsing"""
#     results = []
#     debug_info = []
    
#     try:
#         # Validate request
#         if 'resumes' not in request.files:
#             return jsonify({"error": "No resumes uploaded"}), 400
            
#         uploaded_files = request.files.getlist("resumes")
#         if not uploaded_files or not uploaded_files[0].filename:
#             return jsonify({"error": "No files selected"}), 400

#         # Ensure upload directory exists
#         os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        
#         # Load job descriptions
#         cursor = mysql.connection.cursor()
#         cursor.execute("SELECT id, title, description FROM job_descriptions")
#         job_descriptions = cursor.fetchall()
#         cursor.close()
        
#         debug_info.append(f"Loaded {len(job_descriptions)} job descriptions")
        
#         # Initialize matcher
#         matcher = ResumeMatcher()
        
#         # Process each file
#         for file in uploaded_files:
#             if not file or file.filename == '':
#                 continue
                
#             if not allowed_file(file.filename):
#                 debug_info.append(f"Skipped invalid file type: {file.filename}")
#                 continue
                
#             try:
#                 # Save file
#                 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#                 safe_filename = f"{timestamp}_{file.filename.replace(' ', '_')}"
#                 filepath = os.path.join(UPLOAD_FOLDER, safe_filename)
#                 file.save(filepath)
                
#                 # Extract text
#                 debug_info.append(f"Processing: {file.filename}")
#                 resume_text = extract_text_from_resume(filepath)
                
#                 if not resume_text or len(resume_text) < 100:
#                     debug_info.append("Warning: Insufficient text extracted")
#                     results.append({
#                         "filename": file.filename,
#                         "status": "Error",
#                         "error": "Text extraction failed",
#                         "match": 0
#                     })
#                     continue
                
#                 debug_info.append(f"Extracted {len(resume_text)} characters")
                
#                 # Find best match
#                 best_match = {
#                     "score": 0,
#                     "job_title": "No Match Found",
#                     "job_id": None,
#                     "debug": []
#                 }
                
#                 for job_id, title, description in job_descriptions:
#                     if not description or len(description) < 50:
#                         continue
                        
#                     try:
#                         score = matcher.calculate_match_score(resume_text, description)
#                         best_match["debug"].append(
#                             f"Match with '{title[:30]}': {score:.1f}%"
#                         )
                        
#                         if score > best_match["score"]:
#                             best_match.update({
#                                 "score": score,
#                                 "job_title": title,
#                                 "job_id": job_id
#                             })
                            
#                             if score >= 85:  # Early exit for high matches
#                                 break
                                
#                     except Exception as e:
#                         logger.error(f"Match failed for {title}: {str(e)}")
#                         continue
                
#                 # Determine status
#                 if best_match["score"] >= 80:
#                     status = "Highly Qualified"
#                 elif best_match["score"] >= 50:
#                     status = "Qualified"
#                 else:
#                     status = "Not Qualified"
                
#                 # Add result
#                 results.append({
#                     "filename": file.filename,
#                     "job_id": best_match["job_id"],
#                     "job_title": best_match["job_title"],
#                     "match": round(best_match["score"], 1),
#                     "status": status,
#                     "debug": sanitize_debug_info(best_match["debug"][:3])  # Top 3 matches
#                 })
                
#             except Exception as e:
#                 logger.error(f"Failed processing {file.filename}: {str(e)}")
#                 results.append({
#                     "filename": file.filename,
#                     "status": "Error",
#                     "error": str(e)
#                 })
#                 continue
                
#     except Exception as e:
#         logger.critical(f"API error: {str(e)}", exc_info=True)
#         return jsonify({
#             "error": "Processing failed",
#             "details": str(e),
#             "debug_info": sanitize_debug_info(debug_info)
#         }), 500
        
#     finally:
#         # Clean up uploaded files
#         for file in uploaded_files:
#             if file and file.filename:
#                 try:
#                     os.remove(os.path.join(UPLOAD_FOLDER, file.filename))
#                 except:
#                     pass
    
#     return jsonify({
#         "results": results,
#         "debug_info": sanitize_debug_info(debug_info),
#         "processed": len(results),
#         "errors": len(uploaded_files) - len(results)
#     })

@main_routes.route("/api/parse-resumes", methods=["POST"])
@token_required
def parse_resumes_api(current_user):
    """API endpoint for resume parsing"""
    results = []
    debug_info = []
    saved_files = []

    try:
        if 'resumes' not in request.files:
            return jsonify({"error": "No resumes uploaded"}), 400

        uploaded_files = request.files.getlist("resumes")
        if not uploaded_files or not uploaded_files[0].filename:
            return jsonify({"error": "No files selected"}), 400

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Load job descriptions
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, title, description FROM job_descriptions")
        job_descriptions = cursor.fetchall()
        cursor.close()
        debug_info.append(f"Loaded {len(job_descriptions)} job descriptions")

        matcher = ResumeMatcher()

        for file in uploaded_files:
            if not file or file.filename == '':
                continue

            if not allowed_file(file.filename):
                debug_info.append(f"Skipped invalid file type: {file.filename}")
                continue

            try:
                # Save file with a safe filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                safe_filename = f"{timestamp}_{file.filename.replace(' ', '_')}"
                filepath = os.path.join(UPLOAD_FOLDER, safe_filename)
                file.save(filepath)
                saved_files.append(filepath)

                debug_info.append(f"Processing: {file.filename}")
                resume_text = extract_text_from_resume(filepath)

                if not resume_text or len(resume_text) < 100:
                    debug_info.append("Warning: Insufficient text extracted")
                    results.append({
                        "filename": file.filename,
                        "status": "Error",
                        "error": "Text extraction failed",
                        "match": 0
                    })
                    continue

                debug_info.append(f"Extracted {len(resume_text)} characters")

                best_match = {
                    "score": 0,
                    "job_title": "No Match Found",
                    "job_id": None,
                    "debug": []
                }

                for job_id, title, description in job_descriptions:
                    if not description or len(description) < 50:
                        continue

                    try:
                        score = matcher.calculate_match_score(resume_text, description)
                        best_match["debug"].append(
                            f"Match with '{title[:30]}': {score:.1f}%"
                        )

                        if score > best_match["score"]:
                            best_match.update({
                                "score": score,
                                "job_title": title,
                                "job_id": job_id
                            })

                            if score >= 85:
                                break

                    except Exception as e:
                        logger.error(f"Match failed for {title}: {str(e)}")
                        continue

                if best_match["score"] >= 80:
                    status = "Highly Qualified"
                elif best_match["score"] >= 50:
                    status = "Qualified"
                else:
                    status = "Not Qualified"

                results.append({
                    "filename": file.filename,
                    "job_id": best_match["job_id"],
                    "job_title": best_match["job_title"],
                    "match": round(best_match["score"], 1),
                    "status": status,
                    "debug": sanitize_debug_info(best_match["debug"][:3])
                })

            except Exception as e:
                logger.error(f"Failed processing {file.filename}: {str(e)}")
                results.append({
                    "filename": file.filename,
                    "status": "Error",
                    "error": str(e)
                })
                continue

    except Exception as e:
        logger.critical(f"API error: {str(e)}", exc_info=True)
        return jsonify({
            "error": "Processing failed",
            "details": str(e),
            "debug_info": sanitize_debug_info(debug_info)
        }), 500

    finally:
        for path in saved_files:
            try:
                os.remove(path)
            except Exception as e:
                logger.warning(f"Failed to delete temp file {path}: {str(e)}")

    return jsonify({
        "results": results,
        "debug_info": sanitize_debug_info(debug_info),
        "processed": len(results),
        "errors": len(uploaded_files) - len(results)
    })

