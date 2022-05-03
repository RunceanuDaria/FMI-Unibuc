from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from blockchain import ADMIN_PUBLIC_KEY
from client import Client


ADMIN_PRIVATE_KEY = "3082025e02010002818100ead08f972b7a6b723fc3dac52c3da01efb0054a1f2f876de38f96d577b46d598dd82993800f3188a065d94ecc2e7aea72267bfc0c5af02c51c249720f158308a3d6db563b7e67228fdc8928dd7f7f638c1c525813d94125140d9fc561a244f618070aefaa6b027de3a644327cacc153f82159e61977ca30db6ccc0baea4c9a7702030100010281800b3ce50a5e95d2cb9a7aa49f382150e6faab46e1a34fb9dca3cc682bbe262335d830166624417e24a8ee54a0ca292d662952decdfa88083167c9e683b899386565d546a2f636d2e729c6cb38d75a4671e8e923dfaa035d1a1a9e6e211de58e943c87f3e274e627bbf97bc07ac7307d9440fc0c7df6059d3a1963b63255908139024100ed69d1b9141eb4cc821cee809121ecfeeac0b8f19b03b3e93b5425dfca49ce6cf62d9c997570e92db91aab44bc8a608b3f70aa5d833a50bdbec101eeeb40cc3f024100fd32a8ebfd0c7ea33b8fcf0379eba41587ec7c7e2d7a71cb2be19948ce8dc882ff88b342660bbb64c8f8cafa777bb72c70a7331b6bd4afa0849c3eef9a1883c9024100c0680730c08e96263bb8a8ce0751005a23f4a6ae1fdc235d7cd8988d42cb0801a48d98a181dd4d0ce23c2bdb5c15a56294ba8147a2078bd20b1b2eaeeb77ab4f024100f3bb838e7fee3a2d89d57a729f37ada1285206d933902de065626abb0252cbd50685220265d71f51fa803c6c74fe3baae4da9ec0e3c13e3b27cc7c6d0b8a53b90241008deab72c6175b6a15312b8cba0a9d3566f877c0128a490dbc58137e259de2744358a3498dc3c05db47fa557b809c6e1d06bfca11e9c509a7916ea37a10ac00d2"

app = Flask(__name__)
CORS(app)
admin_client = Client(
    public_key=ADMIN_PUBLIC_KEY,
    private_key=ADMIN_PRIVATE_KEY)


# App
@app.route('/')
def index():
    return render_template('index.html')


# API
@app.route('/post/give/right', methods=["POST"])
def giveRightToVote():
    receiver = request.form['receiver']
    admin_client.createTransaction(receiver)
    return jsonify({"message": "OK"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
