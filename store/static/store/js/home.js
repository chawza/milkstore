var browseitems = 12
var browsepage = 1

var productlists
var shoppinglist

function getproductlist(){
    // create object that handles request
    var req = new XMLHttpRequest()

    // create connection to server
    req.open("GET", `getproductlist/${browseitems}/${browsepage}`)

    // decide what to do when we get HTTP response
    req.onload = function() {
        productlists = JSON.parse(req.response)
    }   
    //send now
    req.send()
}

function renderProductLIst(){
    var productbrowser = $("#product-list-area")
    productbrowser.html("")

    // if products have not recieved from server
    console.log(productlists.items.length)
    if(productlists.items.length == 0){
        productbrowser.html("No product!")
        return
    }

    var browse_content = ''

    for(product of productlists.items){
        img_url = location.origin + '/products/img/' + product.id

        browse_content += `
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
    }
    productbrowser.append(browse_content)
}

getproductlist()
setInterval(renderProductLIst(), 1000)