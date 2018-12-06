
$(function() {
    $('input[name="status"]').on('click', function() {
        if ($(this).val() == '0') {
            $('#id_reason_reject').show();
        }
        else {
            $('#id_reason_reject').hide();
        }
    });
})
