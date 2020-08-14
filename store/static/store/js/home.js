let browseitems = 12
let browsepage = 1

let productlists = []
let shoppinglist = []

function getproductlist(){
    // create object that handles request
    var req = new XMLHttpRequest()

    // create connection to server
    req.open("GET", `getproductlist/${browseitems}/${browsepage}`, false)

    // decide what to do when we get HTTP response
    req.onload = function() {
        productlists = JSON.parse(req.response).items
    }   
    //send now
    req.send()
}

function renderProductLIst(){
    var productbrowser = $("#product-list-area")
    productbrowser.html("")

    // if products have not recieved from server
    if(productlists.length == 0){
        productbrowser.html("No product!")
        return
    }

    //iterate over product list to render the html
    var browse_content = ''
    for(product of productlists){
        img_url = location.origin + '/products/img/' + product.id

        browse_content = `
        <div class="col-4">
            <div class="card h-100">
                <img src="${img_url}" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">${product.name}</h5>
                    <h6 class="card-subtitle">${product.brand}</h6>
                    <h4>Rp. ${product.price}</h4>
                    <button class="btn btn-primary">+</button>
                    <button class="btn btn-primary">-</button>
                </div>
            </div>
        </div>
        `
        productbrowser.append(browse_content)
    }
}

getproductlist()
renderProductLIst()