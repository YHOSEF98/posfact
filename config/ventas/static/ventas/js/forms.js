var ventas = {
    items : {
        cli: '',
        date_joined:'',
        suctotal:0.00,
        total: 0.00,
        products: []
    },
    list: function(){
        $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            data: this.items.products,
            columns: [
                {"data": "id"},
                {"data": "name"},
                {"data": "cat.name"},
                {"data": "pvp"},
                {"data": "cant"},
                {"data": "subtotal"},
            ],
            columsDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row){
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"</i></a>';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row){
                        return '$'+parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row){
                        return '<input type="text"name="cant" class="form-control form-control-sm" autocomplete="off">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row){
                        return '$'+parseFloat(data).toFixed(2);
                    }
                },
            ]
        })
    }
}