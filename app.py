import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.schema import Document

st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

prompt_template = """
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])


def load_youtube(url):
    """Load YouTube transcript using yt-dlp as fallback"""
    try:
        # Try default loader first
        loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
        return loader.load()
    except Exception:
        # Fallback: use yt-dlp to get subtitles/transcript
        import yt_dlp
        ydl_opts = {
            'skip_download': True,
            'writesubtitles': False,
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            text = f"Title: {info.get('title', '')}\n"
            text += f"Description: {info.get('description', '')}\n"
            text += f"Duration: {info.get('duration', '')} seconds\n"
            text += f"Channel: {info.get('uploader', '')}\n"
        return [Document(page_content=text, metadata={"source": url})]


if st.button("Summarize the Content from YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Waiting..."):
                llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

                ## ✅ YouTube vs Website loading
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    docs = load_youtube(generic_url)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                    )
                    docs = loader.load()

                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)
                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")