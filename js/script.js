document.addEventListener('DOMContentLoaded', function () {
      const buttons = document.querySelectorAll('.accordion-button');

      buttons.forEach(button => {
        button.addEventListener('click', function () {
          const content = this.nextElementSibling;
          const detailId = this.getAttribute('data-detail');

          if (this.classList.contains('active')) {
            this.classList.remove('active');
            content.style.display = 'none';
            document.getElementById(detailId).style.display = 'none';
          } else {
            document.querySelectorAll('.accordion-button').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.accordion-content').forEach(cont => cont.style.display = 'none');
            document.querySelectorAll('.detail-content').forEach(detail => detail.style.display = 'none');

            this.classList.add('active');
            content.style.display = 'block';
            document.getElementById(detailId).style.display = 'block';
          }
        });
      });
    });