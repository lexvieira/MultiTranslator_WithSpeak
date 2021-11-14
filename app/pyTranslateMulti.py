#Using Google Translator to Translate words and sentences.
from app.google_trans_new.google_trans_new import google_translator  
import gtts
import base64
def translate(text):
    if text != "":
        to_translate = text
        # print(text)
        
        translations = []    
        # translations["text"] = text

        translator = google_translator()
        
        lang_list = {"en": "English","pt-br":"Portuguese BR","th": "Thai", "es": "Spanish", "fr": "French", "pl": "Polish", "it": "Italian"}
        language = translator.detect(to_translate)
        
        #CreateTokenforTheAudioFile
        language_to_translate = { language[0] : language[1] }
        filename = "translation_lang.mp3"
        for k, l in lang_list.items():
            translate_text = translator.translate(to_translate,lang_src='auto',lang_tgt=k)  
            
            tts = gtts.gTTS(translate_text, lang=k) 
            tts.save(filename.replace("_lang","_" + k))

            with open(filename.replace("_lang","_" + k), "rb") as f1:
                base64encode = base64.b64encode(f1.read()).decode('ascii')
                f1.close()
            
            # return basereturn
            translations.append({"lang_code": k,"language": l, "translation": translate_text, "audio": "data:audio/mpeg;base64," + str(base64encode) })
        
        return { "text": text, "language": language_to_translate, "translations": translations}, 200
    else: 
        return { 'Error': 'Bad Request!' }, 400