$(document).ready(function () {
    const ticketBtn = $('.ticket-btn');
    const form = $('form');
    const imageUpload = $('#upload-image');
    const imageBase64 = $('#imagebase64');
    const imgCrop = $('#img-crop');
    const privacyPopup = $('label[for=privacy]');
    const popup = $('.popup');
    const closePopup = $('.close');
    const privacyInput = $('#privacy');
    let $uploadCrop;

    function readFile(input) {
        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.onload = function (e) {
                $uploadCrop.croppie('bind', {
                    url: e.target.result
                });
                $('.ready').addClass('active');
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    $uploadCrop = imgCrop.croppie({
        viewport: {width: 200, height: 120},
        enableOrientation: true,
        mouseWheelZoom: 'ctrl'
    });

    imageUpload.on('change', function () {
        readFile(this);
    });

    ticketBtn.on('click', function () {
        form.addClass('active');
    });

    privacyPopup.on('click', function () {
        if (privacyInput[0].checked === true)
            popup.addClass('active');
        else {
            popup.removeClass('active')
        }
    });

    closePopup.on('click', function () {
        popup.removeClass('active');
    });

    form.on('submit', function (e) {
        e.preventDefault();
        e.stopPropagation();
        $uploadCrop.croppie('result', {
            type: 'canvas',
            size: 'original'
        }).then(function (resp) {
            imageBase64.val(resp);
            console.log(form.serializeArray());
            $.ajax({
                url: '/apply/',
                method: 'post',
                data: form.serializeArray(),
                success: function (res) {
                    console.log(res)
                }, error: function (err) {
                    console.log(err)
                }
            })
        });
    });

});