<script>


$(function () {
	re_plot();

	function re_plot() {
		var from = parseInt($("#x").val());
		var to = parseInt($("#y").val());
    var points = parseInt($("#points").val());

    if (points <1)
    {
      points = 10;
    }
    var hop = (to-from)/points;

    let input_fun = ($("#func").val());
    let fun = input_fun;

    var d1 = [];

		for (var x = from; x <= to; x += hop)
		{
      var di = [x, eval(fun)]

			d1.push(di);
		}


    var plot_conf = {
      series: {
        lines: {
          show: true,
          lineWidth: 1
        }
      }
    };

		$.plot($("#placeholder"), [
			{
        color: 4,
				data: d1,
				lines: { show: true, fill: false }
			},
		], plot_conf);


		return false;
	}


	$("#redraw").click(function (e) {
        e.preventDefault();
        re_plot();
    });
});
</script>
