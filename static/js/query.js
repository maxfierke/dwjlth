$('#search').submit(function (e) {
	if(e.preventDefault) e.preventDefault(); else e.returnValue = false;
	$.ajax({
		url: "/search",
		dataType: "json",
		data: {'q': $('#query').val()},
		success: function (data, textStatus) {
			$('#notfound').addClass('hidden');
			$('#result').removeClass('hidden');
			$('#restaurant').text(data.restaurant.name);
			if (data.restaurant.verdict) {
				$('#verdict').removeClass('text-error');
				$('#verdict').addClass('text-success');
				$('#verdict').text('Yes, just leave them there.');
			} else {
				$('#verdict').removeClass('text-success');
				$('#verdict').addClass('text-error');
				$('#verdict').text('No, you must bus them yourself.');
			}
		},
		error: function (data, textStatus) {
			$('#result').addClass('hidden');
			$('#notfound').removeClass('hidden');
		}
	});
	return false;
});
