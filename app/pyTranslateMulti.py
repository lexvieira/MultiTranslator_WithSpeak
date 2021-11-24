#Using Google Translator to Translate words and sentences.
from googletrans import Translator  
import gtts
import base64
def translate(text):
    if text != "":
        translator = Translator(service_urls=[
            'translate.google.com'
        ])
        
        to_translate = text
        # print(text)
        
        translations = []    
        
        lang_list = {"en": "English","pt-br":"Portuguese BR","th": "Thai", "es": "Spanish", "fr": "French", "pl": "Polish", "it": "Italian"}
        language = translator.detect(to_translate)
        
        #CreateTokenforTheAudioFile
        language_to_translate = { language[0] : language[1] }
        filename = "translation_lang.mp3"
        for k, l in lang_list.items():
            lang_dest = k
            lang_src = "auto"
            a = translator.translate(to_translate, dest=lang_dest, src = lang_src)            
            
            print("text: {}, translate: {}, pronunciation: {}".format(text, a.text, a.pronunciation))
            translation_return = translator.translate(to_translate,lang_src='auto',lang_tgt=k)  
            
            translation_text = "{}".format(a.text) 
            p = translation_return.pronunciation
            
            tts = gtts.gTTS(translation_text, lang=k) 
            tts.save(filename.replace("_lang","_" + k))

            with open(filename.replace("_lang","_" + k), "rb") as f1:
                base64encode = base64.b64encode(f1.read()).decode('ascii')
                f1.close()

            if p != None:
                translation_text = "{} ({})".format(translation_text, p)
                            
            # return basereturn
            translations.append({"lang_code": k,"language": l, "translation": translation_text, "audio": "data:audio/mpeg;base64," + str(base64encode) })
        
        return { "text": text, "language": language_to_translate, "translations": translations}, 200
    else: 
        return { 'Error': 'Bad Request!' }, 400