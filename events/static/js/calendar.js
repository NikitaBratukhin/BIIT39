document.addEventListener('DOMContentLoaded', function () {
    var events = JSON.parse(eventsData);

    function createCalendar() {
        const monthNames = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];
        let today = new Date(),
            month = today.getMonth(),
            year = today.getFullYear(),
            firstDay = new Date(year, month, 1).getDay(),
            daysInMonth = 32 - new Date(year, month, 32).getDate();

        let calendarGrid = document.getElementById('calendarGrid');
        calendarGrid.innerHTML = '';

        for (let i = 1; i <= daysInMonth; i++) {
            let dayCell = document.createElement('div');
            dayCell.classList.add('day');
            dayCell.setAttribute('data-day', i);
            dayCell.innerHTML = i;

            events.forEach(event => {
                let eventDate = new Date(event.fields.date);
                if (eventDate.getDate() === i && eventDate.getMonth() === month && eventDate.getFullYear() === year) {
                    dayCell.style.background = '#b5f7b7'
                }
            });

            dayCell.addEventListener('click', function () {
                openModal(i, month, year);
            });
            calendarGrid.appendChild(dayCell);
        }
    }

    function openModal(day, month, year) {
        let modal = document.getElementById('eventModal');
        document.getElementById('eventTitle').innerHTML = "<h2>" + `Мероприятия ${day} числа` + "</h2>";

        var events = JSON.parse(eventsData);
        var s = '<br>';
        events.forEach(event => {
            let eventDate = new Date(event.fields.date);
            if (eventDate.getDate() === day && eventDate.getMonth() === month && eventDate.getFullYear() === year) {
                s += `<h4>Название мероприятия: ${event.fields.title}<br>Описание мероприятия: ${event.fields.description}<br>Дата: ${event.fields.date.split('T')[0]}</h4><br>`;
                // Здесь создаем кнопку для записи на мероприятие
                
                s += `<button class="btn btn-success" onclick="location.href='/events/register/${event.pk}'">Записаться на мероприятие: ${event.fields.title}</button><br>`;
            }
        });
        if (s === '<br>') {
            s = "<h4>Мероприятия в эту дату отсутствуют.</h4>";
        }
        document.getElementById('eventDescription').innerHTML = s;
        modal.style.display = 'block';

        document.getElementById('closeModal').onclick = function () {
            modal.style.display = 'none';
        }
    }

    createCalendar();
    var isAdmin = true; // Должно устанавливаться на основе данных с сервера
    if (isAdmin) {
        document.getElementById('adminButtons').style.display = 'flex';
    }
});
