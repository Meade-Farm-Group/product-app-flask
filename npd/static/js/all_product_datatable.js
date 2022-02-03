// TESTING AJAX CALL
// $(document).ready(function() {
//     table = $('#all_product_table').DataTable({
//         "ajax": "../products/all_product_json",
//         "columns": [
//             { "data": "id" },
//             { "data": "name" },
//             { "data": "department" },
//             { "data": "customer" },
//             { "data": "start_date" },
//             { "data": "status" },
//             { "data": "created_on" },
//             { "data": "created_by" },
//             { "data": "action" }
//         ],
//         "columnDefs": [{
//             "targets": -1,
//             "data": "id",
//             "render": function(data, type, row) {
//                 return `
//                     <a href="../products/${data}" class="btn btn-success">
//                         View <i class="fas fa-eye"></i>
//                     </a>
//                 `
//             }
//         }]
//     });
//     setInterval(function() {
//         table.ajax.reload();
//     }, 5000);
// } );
$(document).ready(function() {
    $("#all_product_table").DataTable();
})