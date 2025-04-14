
let deleteitem=(product_id) => {
 swal.fire({
    title: "هل أنت متأكد؟",
    text: " لا يمكنك التراجع عن هذا الاجراء بعد الحذف,",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#3085d6",
    confirmButtonText: "نعم, احذف!",
    cancelButtonText: "لا, الغاء!",


}).then((result) => {
    if (result.isConfirmed) {
        $.ajax({
            url: '/delete/' + product_id + '/',
            type: 'GET',
            success: function(response) {
                swal.fire("تم الحذف!", "تم حذف العنصر بنجاح.", "success").then(() => {
                    window.location.href = '/showcategories/';
                });
            },
            error: function() {
                swal.fire("خطأ!", "حدث خطأ أثناء الاتصال بالخادم.", "error");
            }
        });
    }
});}
