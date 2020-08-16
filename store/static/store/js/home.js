let browseitems = 12
let browsepage = 1

let productlists = []
let shoppinglist = {
    user: "No User",
    items : {}
}

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

function add_shopping_list(pk){
    let item = "item-"+ pk  //accessing the item insinde shoppinglists

    //define the item if the product has not been added to the shopping list
    if(shoppinglist.items[item] == null){
        shoppinglist.items[item] = {}   //declare before define the property
        
        //clone the product detail into shopping list
        shoppinglist.items[item].product = productlists.filter(function(a){
            return a.id == pk
        })[0]
        shoppinglist.items[item].qty = 0
    }
        
    
    //increment the number of items
    shoppinglist.items[item].qty += 1
}

function sub_shopping_list(pk){
    let item = "item-"+ pk //string to access the product in shopping list
    
    // if the item was never on list, don't do anything
    if(shoppinglist.items[item] == null)
        return

    // subtract the value
    shoppinglist.items[item].qty -= 1

    //if the item number is below 1, we discard the item from list
    if(shoppinglist.items[item].qty <= 0)
        delete shoppinglist.items[item]
}

function calculateShoppingDetail(){
    let amount = 0
    let n_product = Object.keys(shoppinglist.items).length
    let n_items = 0

    //iterate over shopping list to sum the amount
    for (itemlist in shoppinglist.items){
        item = shoppinglist.items[itemlist]

        amount += item.qty * item.product.price
        n_items += item.qty
    }

    //assign the value
    $("#total-amount").html('RP. ' + amount)
    $("#number-product").html(n_product + ' products')
    $("#number-items").html(n_items + ' items')
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

        // define the tamplate to add
        browse_content = `
        <div class="col-4">
            <div class="card h-100">
                <img src="${img_url}" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">${product.name}</h5>
                    <h6 class="card-subtitle">${product.brand}</h6>
                    <h4>Rp. ${product.price}</h4>
                    <button id="btn-add-${product.id}" class="btn btn-primary" value="add-${product.id}">+</button>
                    <button id="btn-sub-${product.id}" class="btn btn-primary" value="sub-${product.id}">-</button>
                </div>
            </div>
        </div>
        `
        //append the tags at the end of product list area
        productbrowser.append(browse_content)

        //add event function when the buttons are click
        $("#btn-add-"+product.id).click(function(){
            add_shopping_list(this.value.split("-")[1])
            renderShoppingList()
        })

        $("#btn-sub-"+product.id).bind('click', function(){
            sub_shopping_list(this.value.split("-")[1])
            renderShoppingList()
        })
    }
}

function renderShoppingList(){
    let shoppinglist_area = $("#shopping-list-area")
    shoppinglist_area.html("")
    let amount = 0
    let n_product = Object.keys(shoppinglist.items).length
    let n_items = 0

    for (itemlist in shoppinglist.items){
        item = shoppinglist.items[itemlist]
        
        let template = `
            <li id="product-${item.product.id}" class="list-group-item">
                <div class="row">
                    <div class="col-8">
                        <h5 class="card-title">${item.product.name}</h6>
                    </div>
                    <div class="col-4">
                        <button id="btn-del-${item.product.id}" type="button" class="btn btn-alert">X</button>
                    </div>
                </div>
                <p class="card-subtitle">price : ${item.product.price}</p>
                <p class="card-subtitle">quantity : ${item.qty}</p>
            </li>
        `
        //append the template
        shoppinglist_area.append(template)

        // add function to the delete button
        $("#btn-del-" + item.product.id).click(function(){
            // delete the selected product from the list
            delete shoppinglist.items['item-' + item.product.id]

            // delete the element list
            $("#product-" + item.product.id).remove()

            // render the recalculated shopping list
            calculateShoppingDetail()
        })

        // sum the caculation for card's body
        amount += item.qty * item.product.price
        n_items += item.qty
    }

    $("#total-amount").html('RP. ' + amount)
    $("#number-product").html(n_product + ' products')
    $("#number-items").html(n_items + ' items')
}

getproductlist()
renderProductLIst()