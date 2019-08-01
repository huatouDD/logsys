$(function () {

    var email = "";
    var password = "";
    var is_login = false;
    var csrf_token = "";
    var is_error = false;

    function isEmpty(obj) {
        if (typeof obj == "undefined" || obj == null || obj == "") {
            return true;
        } else {
            return false;
        }
    }


    $('#sub').on("click", function () {
        email = $('#email').val();
        password = $('#password').val();
        csrf_token = $("#csrf_token").attr("value");

        var data = {
            "email": email,
            "password": password,
            "csrf_token": csrf_token
        };

        if (isEmpty(email)) {
            is_error = true;
            $("#user_error").css('display', 'block');
            $("#user_error").text("* 用户名不能为空");
        }
        ;

        if (isEmpty(password)) {
            is_error = true;
            $("#password_error").css('display', 'block');
            $("#password_error").text("* 用户名不能为空");
        }
        ;


        if (!is_error) {
            is_login = true;
            $.ajax({
                url: "/login_api/",
                type: "POST",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(data),
                success: function (resp) {
                    if (resp.code == '0') {
                        location.href = '/index';
                    }
                },
                error: function (resp) {
                    try {
                        var data = resp.responseJSON;
                        var errors = data.response.errors;
                        if (errors['password']) {
                            $("#password_error").css('display', 'block');
                            $("#password_error").text(errors['password']);

                        }
                        is_login = false;

                    } catch (e) {
                        alert('1111111111111111111111');
                        location.href = "/"
                    }
                }
            });
        }


    });
});