$(document).ready(function() {

	$('#datepicker').datepicker({
	    format: "yyyy-mm-dd",
	    defaultDate: new Date(),
	    todayHighlight: true,
	    todayBtn: "linked",
	    toggleActive: true
	});

	$('#datepicker').datepicker('update', new Date());

	$('#input_date').val(
	        $('#datepicker').datepicker('getFormattedDate')
    );

	$('.'+ $('#input_date').val()).show();

	var totals=[0,0,0];
	var $dataRows=$('.'+$('#input_date').val());
    $dataRows.each(function() {
        $(this).find('.rowDataSd').each(function(i){        
            totals[i]+=parseFloat( $(this).html());
        });
    });
    $("#sum_table td.totalCol").each(function(i){  
        $(this).html(totals[i]+" Rs");
    });


	$('#datepicker').on('changeDate', function() {
	    $('#input_date').val(
	        $('#datepicker').datepicker('getFormattedDate')
    	);
    	$('.collapse').hide();
    	$('.'+ $('#input_date').val()).show();

    	var totals=[0,0,0];
    	var $dataRows=$('.'+$('#input_date').val());
	    $dataRows.each(function() {
	        $(this).find('.rowDataSd').each(function(i){        
	            totals[i]+=parseFloat( $(this).html());
	        });
	    });
	    $("#sum_table td.totalCol").each(function(i){  
	        $(this).html(totals[i]+" Rs");
	    });

    });

})