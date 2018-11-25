from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/upload')
def upload_file():
    return render_template("/upload.html")


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        # Do sth with the file here, e.g.
        # f.save(secure_filename(f.filename))
        meta_dict_1 = [
            {
                "file": "database/dress1.png",
                "retailer": "Forever 21",
                "price": 38.00,
                "rating": 5,
                "confidence": 0.7,
                "url": "https://www.forever21.com/ca/shop/catalog/product/f21/dress/2000290193/02?esvt=2148-GOCAE136250&esvq=&esvadt=999999-0-47968-1&esvcrea=270357890322&esvplace=&esvd=c&esvtg=pla-442111455276&esvo=2000290193024&esvaid=50184&gclid=CjwKCAiAiuTfBRAaEiwA4itUqE1gNQJIhwLRK2LxZGDJAhxrroqBlm3_z-snkfFY1wBn0dRWl32cQhoCxdkQAvD_BwE"
            },
            {
                "file": "database/dress2.png",
                "retailer": "American Apparel",
                "price": 36.00,
                "rating": 3,
                "confidence": 0.95,
                "url": "http://www.americanapparel.com/en/cotton-2x2-sofia-dress_ctw3309w?c=Black"
            },
            {
                "file": "database/dress3.png",
                "retailer": "Forever 21",
                "price": 38.00,
                "rating": 4,
                "confidence": 0.75,
                "url": "https://urban-planet.com/products/0032-42639080-plunging-v-neck-side-slit-bodycon-maxi-dress"
            },
            {
                "file": "database/dress4.png",
                "retailer": "Hudson's Bay",
                "price": 249.00,
                "rating": 5,
                "confidence": 0.90,
                "url": "https://www.thebay.com/main/ProductDetail.jsp?PRODUCT%3C%3Eprd_id=845524441996652&&site_refer=CSE_GGLPLA&gclid=CjwKCAiAiuTfBRAaEiwA4itUqN5O0njC5ISaS3kaKny355G3CNgE4F_ZMiPQZAPvxLgnvvFhIs4aHhoCupwQAvD_BwE&gclsrc=aw.ds"
            }
        ]
        return json.dumps(meta_dict_1)


if __name__ == '__main__':
    app.run(debug=True)
