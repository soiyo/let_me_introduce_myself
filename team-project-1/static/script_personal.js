$(document).ready(function () {
    show();
});
function show() {
    $.ajax({
        type: 'GET',
        url: '/profile',
        data: {},
        success: function (response) {
            let rows = response['intro'];
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name'];
                let hi = rows[i]['hi'];

                let temp_html = ` <tr>
                                <td>${name}</td>
                                <td>${hi}</td> 
                            </tr>`;
                $('#box').append(temp_html);
            }
        },
    });
}
function save() {
    let name = $('#name').val();
    let hi = $('#hi').val();

    $.ajax({
        type: 'POST',
        url: '/profile',
        data: { name_give: name, hi_give: hi }, //데이터 전송 (app.py로)
        success: function (response) {
            alert(response['msg']); //메세지 띄우기
            window.location.reload(); //다 가져오면 새로고침
        },
    });
}
