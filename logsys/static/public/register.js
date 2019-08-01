$(function () {
    var email = '';
    var password = '';
    var re_password = '';
    var is_error = false;  //判断参数是否为空

    function isEmpty(obj) {
        if (typeof obj == "undefined" || obj == null || obj == "") {
            return true;
        } else {
            return false;
        }
    }


    // 注册按钮点击
    $("#sub").on('click', function () {
        email = $('#email').val();
        password = $('#password').val();
        re_password = $('#re_password').val();
        is_error = false;

        if (isEmpty(email)) {
            is_error = true;
            swal({text: '请输入用户名', type: 'error', width: "320px"});
            return false;
        }

        if (isEmpty(password)) {
            is_error = true;
            swal({text: '请输入密码', type: 'error', width: "320px"});
            return false;
        }

        if (isEmpty(re_password)) {
            is_error = true;
            swal({text: '请输入确认密码', type: 'error', width: "320px"});
            return false;
        }

        var data = {
            'email': email,
            'password': password,
            're_password': re_password,
        };

        if (!is_error) {
            $.ajax({
                url: '/register',
                type: 'POST',
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(data),
                success: function (resp) {
                    if (resp.code == "0") {
                        location.href = '/index';
                    } else {
                        var errors = resp.msg;
                        // 密码错误提示
                        if (errors['password']) {
                            swal({text: '两次密码输入不一致', type: 'error', width: "320px"});
                            return false;
                        }
                        //用户名重复提示
                        if (errors['email']) {
                            swal({text: '该用户名已被使用', type: 'error', width: "320px"});
                            return false;
                        }
                    }
                }
            })
        }
        return false //阻止页面刷新
    })
});