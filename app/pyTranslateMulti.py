#Using Google Translator to Translate words and sentences.
from app.google_trans_new.google_trans_new import google_translator  
import gtts
import base64
import librosa
def translate(text):
    if text != "":
        to_translate = text
        # print(text)
        
        translations = []    
        # translations["text"] = text

        translator = google_translator()
        
        lang_list = {"en": "English","pt-br":"Portuguese BR","th": "Thai", "es": "Spanish", "fr": "French", "pl": "Polish"}
        language = translator.detect(to_translate)
        
        
        #CreateTokenforTheAudioFile
        language_to_translate = { language[0] : language[1] }
        filename = "translation_lang.mp3"
        for k, l in lang_list.items():
            # print("{} - {}".format(k,l))
            translate_text = translator.translate(to_translate,lang_src='auto',lang_tgt=k)  
            # print("{} - {}".format(l,translate_text))
            
            tts = gtts.gTTS(translate_text, lang=k) 
            tts.save(filename.replace("_lang","_" + k))

            # print(tts)

            with open(filename.replace("_lang","_" + k), "rb") as f1:
                base64encode = base64.b64encode(f1.read())
                
            # print(base64encode)
            
            # return basereturn
            translations.append({"lang_code": k,"language": l, "translation": translate_text, "audio": "data:audio/mp3;base64," + str(base64encode) })

        # print(translations)
        
        # basereturn =  base64.b64encode(tts.audio_content).decode()
        

        # with open("0.wav", "rb") as f1,open("b64.txt", "w") as f2:
        #     encoded_f1 = base64.b64encode(f1.read())
            # f2.write("data:audio/wav;base64,")
            # f2.write(str(encoded_f1))
              
        # return base64.b64encode(audio_content)        
        # base64audio = base64.
        # basereturn =  base64.b64encode(tts.audio_content).decode()


        
        return { "text": text, "language": language_to_translate, "translations": translations}, 200
    else: 
        return { 'Error': 'Bad Request!' }, 400