function addcart() {
    $.ajax({
        url: "/addtocart/",
        type: "get",



        success:function (result) {
            console.log(result.cart_count);
            $('.cart-count').text(result.cart_count); // Update the cart count in the HTML element with id "cart"
            Swal.fire({
                title: 'نجاح!',
                text: 'تمت الإضافة إلى السلة بنجاح',
                icon: 'success',
                confirmButtonText: 'موافق',
                timer: 2000, // يختفي تلقائيًا بعد 2 ثانية
                timerProgressBar: true
            });
        }


    });


}


