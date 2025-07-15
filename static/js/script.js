// Counter animation
document.addEventListener('DOMContentLoaded', () => {
  const counters = document.querySelectorAll('.counter');
  counters.forEach(counter => {
    counter.innerText = '0';
    const update = () => {
      const target = +counter.getAttribute('data-target');
      const count = +counter.innerText;
      const inc = target / 200;
      if(count < target) {
        counter.innerText = `${Math.ceil(count + inc)}`;
        setTimeout(update, 10);
      } else {
        counter.innerText = target;
      }
    };
    update();
  });
});
