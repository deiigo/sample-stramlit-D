import streamlit as st
import requests
from PIL import Image
import json
from PIL import ImageDraw
import io

st.title('顔認識アプリ')

SUBSCRIPTION_KEY = 'd81449b6f59a43d7823c6522b464191b'
ENDPOINT = 'https://20210802face.cognitiveservices.azure.com/'
assert SUBSCRIPTION_KEY

face_api_url = ENDPOINT + 'face/v1.0/detect'


uploaded_file = st.file_uploader('Choose an image...',type='jpg')

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    with io.BytesIO() as output:
        img.save(output,format='JPEG')
        binary_img = output.getvalue()  #バイナリ取得

    headers = {
        'content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

    params = {
        'returnFaceId': 'True',
        'returnFaceAttributes':'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup'
    }

    res = requests.post(face_api_url,params = params,
                            headers=headers,data=binary_img)

    results = res.json()

    for result in results:
        rect = result['faceRectangle']

        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'],rect['top']),(rect['left']+rect['width'],rect['top']+rect['height'])],fill=None,outline='green',width=5)

    st.image(img,caption = 'Uploaded Image.' ,use_column_width=True)


































# st.write('データフレーム')
# st.write(
#     pd.DataFrame({
#         '1st column':[1,2,3,4],
#         '2nd column':[10,20,30,40]
#     })
# )

# """
# # My First App
# ## マジックコマンド
# こんな感じでマジックコマンドを使用できる。Markdown対応。
# """

# if st.checkbox('チャート表示'):
#     chart_df = pd.DataFrame(
#         np.random.randn(20,3),
#         columns = ['a','b','c']
#     )

#     st.line_chart(chart_df)



















