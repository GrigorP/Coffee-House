document.addEventListener('DOMContentLoaded', function() {
    $(".filter-checkbox").on("click", function(){ 

        let filter_object = {}
        
               
        $(".filter-checkbox").each(function(){
            let filter_key = $(this).data("category")
            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-category = ' + filter_key + ']:checked')).map(function(element){
                return element.value
            })
        })

        $.ajax({
            url: '/filter-products',
            data: filter_object,
            dataType: 'json',
            success: function(response){
                $("#filtered-products").html(response.Data)
            }
        })
    })
});