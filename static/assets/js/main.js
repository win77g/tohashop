$(document).ready(function () {


//подсчет сум товаров и вывод в итого в корзине и оплате
  function calculatingBasketAmount(){
      var total_order_amount = 0;

      $('.tot').each(function () {

          // console.log($(this).text());

          total_order_amount += parseInt($(this).text());
      });
         $('.total_order_amount').text(total_order_amount.toFixed(2));

  };

  // подсчет количества и суммы в корзине и оплате
  $(document).on('change', "#qty",function () {

      var current_nmb = $(this).val();
      // console.log(current_nmb);
      var current_tr = $(this).closest('tr');
      var current_price = parseInt(current_tr.find('.product-price').text());
      var total_amount = current_nmb * current_price;
      current_tr.find('.tot').text(total_amount.toFixed(2));


      calculatingBasketAmount();
  });
// searchbar
// -------------------------------------------------------------

           $('a[href="#search"]').on('click', function(event) {
                   event.preventDefault();
                   $('#search').addClass('open');
                   $('#search > form > input[type="search"]').focus();
               });

               $('#search, #search button.close').on('click keyup', function(event) {
                   if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
                       $(this).removeClass('open');
                   }
               });
// --------------------------------------панель--------
               $('.cd-btn').on('click', function(event){
               		event.preventDefault();
               		$('.cd-panel').addClass('is-visible');
               	});
               	//clode the lateral panel
               	$('.cd-panel').on('click', function(event){
               		if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
               			$('.cd-panel').removeClass('is-visible');
               			event.preventDefault();
               		}
               	});
// -----------------------------------------------------


});
