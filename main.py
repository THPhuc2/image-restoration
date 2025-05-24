# import requests
# import base64

# API_KEYS = [
#     "AIzaSyCX8zI_mxdn6GOYRXogSsXsVr15b5iEUJM",
#     "AIzaSyDvwkdHeCwoVuT3cIJLVIFlkw0-LblmdAg",
#     "AIzaSyCOO9MTc8Ytx9-PUzpPMYA_MAygpAHKoh8",
#     "AIzaSyD2cfooSLoqMfhJrvU339Mwo3utqzAkW9E",
#     "AIzaSyCMxYblhF9PwWmqioQCDbDIxkthi1LqK4A",
#     "AIzaSyDGNaIg9hk8jGG_QVkj55Vyev2SFlCU1CE"
# ]

# API_URL = "https://generativelanguage.googleapis.com/v1beta"

# WORKING_MODELS = [
#     "models/gemini-1.5-flash-latest",
#     "models/gemini-1.5-flash-001",
#     "models/gemini-1.5-flash-001-tuning",
#     "models/gemini-1.5-flash",
#     "models/gemini-1.5-flash-002",
#     "models/gemini-1.5-flash-8b",
#     "models/gemini-1.5-flash-8b-001",
#     "models/gemini-1.5-flash-8b-latest",
#     "models/gemini-2.5-flash-preview-04-17",
#     "models/gemini-2.5-flash-preview-05-20"
# ]

# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         image_bytes = image_file.read()
#         return base64.b64encode(image_bytes).decode("utf-8")

# def query_model_with_image(model_name, image_path, api_key):
#     url = f"{API_URL}/{model_name}:generateContent?alt=json&key={api_key}"
#     encoded_image = encode_image(image_path)

#     headers = {"Content-Type": "application/json"}
#     data = {
#         "contents": [{
#             "parts": [
#                 {
#                     "text": (
#                         "Bạn hãy phân tích thông tin trong ảnh theo các tiêu chí sau. "
#                         "Nếu ảnh là chân dung một nhà triết học, hãy trả lời theo cấu trúc:\n"
#                         "- Tên:\n"
#                         "- Năm sinh - Năm mất:\n"
#                         "- Các tác phẩm kinh điển:\n"
#                         "- Những đóng góp đối với triết học:\n\n"
#                         "Nếu là một tác phẩm hội họa, hãy trả lời theo cấu trúc:\n"
#                         "- Tên tác phẩm:\n"
#                         "- Họa sĩ:\n"
#                         "- Các tác phẩm tiêu biểu khác:\n"
#                         "- Những đóng góp với triết học :\n\n"
#                         "Nếu là người thường hoặc ảnh không rõ, chỉ cần trả lời: 'Không rõ thông tin triết học'."
#                     )
#                 },
#                 {
#                     "inline_data": {
#                         "mime_type": "image/jpeg",
#                         "data": encoded_image
#                     }
#                 }
#             ]
#         }]
#     }

#     response = requests.post(url, headers=headers, json=data)
#     return response

# def try_models_on_image(image_path):
#     key_index = 0
#     for model in WORKING_MODELS:
#         success = False
#         while key_index < len(API_KEYS):
#             current_key = API_KEYS[key_index]
#             print(f"\n🔍 Trying model: {model} with API key index {key_index}")
#             try:
#                 res = query_model_with_image(model, image_path, current_key)
#                 if res.status_code == 200:
#                     output = res.json()
#                     text = output["candidates"][0]["content"]["parts"][0]["text"]
#                     print(f"✅ Success with {model} (API key index {key_index}):\n{text}")
#                     success = True
#                     break
#                 else:
#                     error_msg = res.json().get('error', {}).get('message', '')
#                     print(f"⚠️ Model failed ({res.status_code}): {error_msg}")
#                     if "quota" in error_msg.lower() or "exceeded" in error_msg.lower():
#                         print(f"⚠️ Quota exceeded for API key index {key_index}, switching to next key...")
#                         key_index += 1
#                     else:
#                         break
#             except Exception as e:
#                 print(f"❌ Exception occurred with {model} (API key index {key_index}): {e}")
#                 key_index += 1
#         if success:
#             return
#     print("\n🚫 All models failed or all API keys quota exceeded.")

# if __name__ == "__main__":
#     image_path = "/home/nhattan05022003/coding/SEM_8/MLN_111/photo_restoration/output_img_folder/final_output/monalisa.png"  # Đổi thành đường dẫn ảnh trên máy bạn
#     try_models_on_image(image_path)

import requests
import base64

API_KEYS = [
    "AIzaSyCX8zI_mxdn6GOYRXogSsXsVr15b5iEUJM",
    "AIzaSyDvwkdHeCwoVuT3cIJLVIFlkw0-LblmdAg",
    "AIzaSyCOO9MTc8Ytx9-PUzpPMYA_MAygpAHKoh8",
    "AIzaSyD2cfooSLoqMfhJrvU339Mwo3utqzAkW9E",
    "AIzaSyCMxYblhF9PwWmqioQCDbDIxkthi1Lq4A",
    "AIzaSyDGNaIg9hk8jGG_QVkj55Vyev2SFlCU1CE"
]

API_URL = "https://generativelanguage.googleapis.com/v1beta"

WORKING_MODELS = [
    "models/gemini-1.5-flash-latest",
    "models/gemini-1.5-flash-001",
    "models/gemini-1.5-flash-001-tuning",
    "models/gemini-1.5-flash",
    "models/gemini-1.5-flash-002",
    "models/gemini-1.5-flash-8b",
    "models/gemini-1.5-flash-8b-001",
    "models/gemini-1.5-flash-8b-latest",
    "models/gemini-2.5-flash-preview-04-17",
    "models/gemini-2.5-flash-preview-05-20"
]

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        return base64.b64encode(image_bytes).decode("utf-8")

def query_model_with_image(model_name, image_path, api_key):
    url = f"{API_URL}/{model_name}:generateContent?alt=json&key={api_key}"
    encoded_image = encode_image(image_path)

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [
                {
                    "text": (
                        "Bạn hãy phân tích thông tin trong ảnh theo các tiêu chí sau. "
                        "Nếu ảnh là chân dung một nhà triết học, một người liên quan tới cách mạng, hãy trả lời theo cấu trúc:\n"
                        "- Tên:\n"
                        "- Năm sinh - Năm mất:\n"
                        "- Các tác phẩm kinh điển:\n"
                        "- Những đóng góp đối với triết học:\n\n"
                        "Nếu là một tác phẩm hội họa, hãy trả lời theo cấu trúc:\n"
                        "- Tên tác phẩm:\n"
                        "- Họa sĩ:\n"
                        "- Các tác phẩm tiêu biểu khác:\n"
                        "- Những đóng góp với triết học :\n\n"
                        "Nếu là người thường hoặc ảnh không rõ, chỉ cần trả lời: 'Không rõ thông tin triết học'."
                    )
                },
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": encoded_image
                    }
                }
            ]
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    return response

def try_models_on_image(image_path):
    key_index = 0
    for model in WORKING_MODELS:
        success = False
        while key_index < len(API_KEYS):
            current_key = API_KEYS[key_index]
            print(f"\n🔍 Trying model: {model} with API key index {key_index}")
            try:
                res = query_model_with_image(model, image_path, current_key)
                if res.status_code == 200:
                    output = res.json()
                    text = output["candidates"][0]["content"]["parts"][0]["text"]
                    print(f"✅ Success with {model} (API key index {key_index}):\n{text}")
                    return text  # Return the description
                else:
                    error_msg = res.json().get('error', {}).get('message', '')
                    print(f"⚠️ Model failed ({res.status_code}): {error_msg}")
                    if "quota" in error_msg.lower() or "exceeded" in error_msg.lower():
                        print(f"⚠️ Quota exceeded for API key index {key_index}, switching to next key...")
                        key_index += 1
                    else:
                        break
            except Exception as e:
                print(f"❌ Exception occurred with {model} (API key index {key_index}): {e}")
                key_index += 1
        if success:
            return ""
    print("\n🚫 All models failed or all API keys quota exceeded.")
    return ""  # Return empty string if all attempts fail

if __name__ == "__main__":
    image_path = "/home/nhattan05022003/coding/SEM_8/MLN_111/photo_restoration/output_img_folder/final_output/monalisa.png"
    description = try_models_on_image(image_path)
    print(f"Final description: {description}")