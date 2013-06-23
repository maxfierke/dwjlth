$(document).ready(function () {
	$('#search').submit(function (e) {
		if(e.preventDefault) e.preventDefault(); else e.returnValue = false;
		$.ajax({
			url: "/search",
			dataType: "json",
			data: {'q': $('#query').val()},
			success: function (data, textStatus) {
				console.log(data);
				$('#notfound').addClass('hidden');
				$('#result').removeClass('hidden');
				console.log(data.restaurant)
				if (data.restaurant.verdict) {
					$('#verdict').removeClass('text-error');
					$('#verdict').addClass('text-success');
					$('#verdict').text('Yes');
				} else {
					$('#verdict').removeClass('text-success');
					$('#verdict').addClass('text-error');
					$('#verdict').text('No');
				}
			},
			error: function (data, textStatus) {
				$('#result').addClass('hidden');
				$('#notfound').removeClass('hidden');
			}
		});
		return false;
	});
});