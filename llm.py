from dotenv import load_dotenv
import os
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
from llama_index.multi_modal_llms.gemini import GeminiMultiModal
from llama_index.multi_modal_llms.generic_utils import load_image_urls



class LLM:
    def __init__(self, place_image_link, api_key) -> None:
        self.image_link = place_image_link
        self.model = GeminiMultiModal(
            model_name="models/gemini-pro-vision", 
            api_key=api_key
        )
        self.image_doc = load_image_urls(self.image_link)

    def describe_image(self):
        image_doc = load_image_urls(self.image_link)
        
        response = self.model.complete(
            prompt="Describe the Images within 100 words",
            image_documents=image_doc
        )
        return response
    
    def hotel_finder(self):
        response = self.model.complete(
            prompt="""Where is this place City and Country tell in one word? 
            Recommend some nearby hotel based on this place""",
            image_documents=self.image_doc
        )
        return response
    
    def custom_query(self, prompt):
        response = self.model.complete(
            prompt=prompt,
            image_documents=self.image_doc
        )
        return response




