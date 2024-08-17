let date_range = null;
let date_now = new moment().format('YYYY-MM-DD');

function FiltradoPorRango() {
    let parametros = {
        'action': 'report_data'
    }
    if (date_range !== null) {
        parametros['start_date'] = date_range.startDate.format('YYYY-MM-DD');
        parametros['end_date'] = date_range.endDate.format('YYYY-MM-DD');
    }
    $('#tabla').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: parametros,
            dataType: 'json',
            dataSrc: ""
        },
        columnDefs: [
            {
                tarjets: [-1,-2,-3,-4,-5],
                class: 'text-center',
                orderable: false,
            }
        ],
        initComplete: function (settings, json){

        }
    });
}
$(function () {
    $('input[name="date_range"]').daterangepicker({
        locale: {
            format: 'YYYY / MM / DD',
            applyLabel: '<i class="fa-solid fa-check fa-beat"></i> Aplicar',
            cancelLabel: '<i class="fa-solid fa-times fa-beat"></i> Cancelar',
        }
    }).on('apply.daterangepicker', function(ev, picker) {
        date_range =  picker;
        FiltradoPorRango();
    }).on('cancel.daterangepicker', function(ev, picker) {
        $(this).data('daterangepicker').setStartDate(date_now);
        $(this).data('daterangepicker').setEndDate(date_now);
        date_range = picker;
        FiltradoPorRango();
    });
    FiltradoPorRango();
});
