from app import create_app
import nltk
from dotenv import load_dotenv
load_dotenv()  # Loads .env file into environment variables

# nltk.download('punkt') 
# nltk.download('stopwords')
# nltk.download('wordnet') # <- run once, then you can remove this

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
