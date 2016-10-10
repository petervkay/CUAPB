

$(document).ready(function(){
	$add_related = $('.related-widget-wrapper-link');
	    $add_related.each(function() {
	      $original_href= $(this).attr('href');
	      if ($original_href) {
		      $new_href = $original_href.substring(0, $original_href.indexOf('?'));
		      $(this).attr('href',$new_href)
		      $(this).attr('target','_blank')

		   	}

	    });
});