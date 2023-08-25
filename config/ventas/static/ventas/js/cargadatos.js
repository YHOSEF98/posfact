function addproductos(){
    $.ajax({
        url:"/ventas/add_venta2/",
        type:"POST",
        datatype:"json",
        success: function(response){
            console.log(response);
        }
    })
}