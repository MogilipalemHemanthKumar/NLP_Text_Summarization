import streamlit as st
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
nltk.download('punkt')

def sumy_summarizer(docx):
    parser=PlaintextParser.from_string(docx,Tokenizer("english"))
    lex_summarizer=LexRankSummarizer()
    summary=lex_summarizer(parser.document,3)
    summary_list=[str(sentence) for sentence in summary]
    result= " ".join(summary_list)
    return result

def main():
    st.title("Text Summarization")
    input_text = st.text_area("Enter text here:")

    if st.button("Summarize"):

       summary = sumy_summarizer(input_text)
       st.success(summary)
if __name__ == "__main__":
    main()
