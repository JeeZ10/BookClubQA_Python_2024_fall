import allure
from playwright.sync_api import Page, expect

from core.settings import base_url

profile_page = "http://testing.misleplav.ru/subscription/profile/"


class Header:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем Хэдер на главной странице")
    def visit(self):
        self.page.goto(base_url)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_login_button(self):
        self.page.get_by_role('link', name="Войти").click()

    @allure.step("Кликаем на кнопку 'Регистрация'")
    def click_registration_button(self):
        self.page.get_by_role('link', name="Регистрация").click()

    @allure.step("Проверяем видимость кнопки 'Создать объявление'")
    def create_listing_button_should_be_visible(self):
        expect(self.page.get_by_test_id("create-listing")).to_be_visible()

    @allure.step("Кликаем на кнопку 'Найти репетитора'")
    def click_find_tutor_button(self):
        self.page.locator("//li/a[text() = 'Найти репетитора']").click()

    @allure.step("Проверяем видимость кнопки 'Поддержка'")
    def support_button_should_be_visible(self):
        button = self.page.locator(
            "//a[contains(@class, 'btn') and text()='Поддержка']"
        )
        expect(button).to_be_visible()

    @allure.step("Кликаем на кнопку 'Поддержка'")
    def click_support_button(self):
        button = self.page.locator(
            "//a[contains(@class, 'btn') and text()='Поддержка']"
        )
        button.click()
        expect(self.page).to_have_url("https://t.me/misleplav_support_bot")

    @allure.step("Наводим мышку на кнопку 'Поддержка' и проверяем изменение цвета")
    def hover_support_button_color_check(self):
        button = self.page.locator(
            "//a[contains(@class, 'btn') and text()='Поддержка']"
        )
        original_color = button.evaluate(
            "el => window.getComputedStyle(el).backgroundColor"
        )
        button.hover()
        expect(button).not_to_have_css("background-color", original_color)

    @allure.step("Проверяем видимость кнопки 'Профиль'")
    def profile_button_should_be_visible(self):
        button = self.page.locator("[data-testid='profile']")
        expect(button).to_be_visible()

    @allure.step("Кликаем на кнопку 'Профиль'")
    def click_profile_button(self):
        button = self.page.get_by_test_id("profile")
        button.click()
        expect(self.page).to_have_url(profile_page)

    @allure.step("Проверяем видимость кнопки 'Войти'")
    def login_button_should_be_visible(self):
        button = self.page.locator(
            '(//a[@class="btn btn-outline-light mb-2 me-2 ms-3"])[1]'
        )
        assert button.is_visible()

    @allure.step("Проверяем видимость кнопки 'Стать репетитором'")
    def become_a_tutor_button_is_visible(self):
        button = self.page.locator(
            "body > main > div > div > section:nth-child(1) > div.d-none.d-sm-flex.justify-content-center.mt-4 > a:nth-child(2)"
        )
        assert button.is_visible()

    @allure.step("Проверяем доступна ли кнопка 'Войти' для взаимодействия")
    def login_button_is_enabled(self):
        button = self.page.locator('//*[@id="navbarNav"]/ul/li[1]/a')
        assert button.is_enabled()

    @allure.step("Проверяем видимость кнопки 'Создать объявление'")
    def click_create_announcement_btn(self):
        button = self.page.locator('//*[@id="navbarNav"]/ul/li[1]/a')
        button.click()
        expect(self.page).to_have_url("http://testing.misleplav.ru/listings/create/")

    @allure.step("Проверяем видимость кнопки 'Статистика '")
    def statistics_button_is_visible(self):
        button = self.page.locator(
            'a.btn.btn-outline-light.mb-2.ms-3[href="/statistics/statistics/"]'
        )
        assert button.is_visible()

    @allure.step("Проверяем видимость кнопки 'Найти репетитора'")
    def find_a_tutor_button_should_be_visible(self):
        button = self.page.locator("//li[@class='nav-item mb-1'][2]")
        assert button.is_visible()

    @allure.step("Кликаем на кнопку 'Статистика'")
    def click_statistics_button(self):
        button = self.page.locator(
            'a.btn.btn-outline-light.mb-2.ms-3[href="/statistics/statistics/"]'
        )
        button.click()
        expect(self.page).to_have_url(
            "http://testing.misleplav.ru/statistics/statistics/"
        )

    @allure.step("Кликаем на кнопку 'Создать объявление' в хедере")
    def click_create_announcement_button(self):
        self.page.locator("a", has_text="Создать объявление").click()

    @allure.step("Проверяем отсутствие кнопки 'Выйти'")
    def check_logout_is_absent(self):
        """Проверка отстутствия кнопки 'Выйти' у незарегистрированного пользователя параметризацией
        для всех доступных страниц
        """
        button = self.page.locator("//a[contains(@class, 'btn') and text()='Выйти']")
        expect(button).not_to_be_attached()

    @allure.step("Проверяем наличие или отсутствие кнопки 'Мое объявление'")
    def check_my_announcement_button_visibility(self, should_be_visible=True):
        button = self.page.locator('a.btn.btn-outline-light:has-text("Мое объявление")')

        if should_be_visible:
            assert button.is_visible(), "Кнопки 'Мое объявление' нет на странице"
        else:
            button_count = button.count()
            assert button_count == 0, "Кнопка 'Мое объявление' присутствует на странице"

    @allure.step("Проверяем отсутствие кнопки 'Мои студенты'")
    def my_students_button_is_hidden(self):
        return self.page.locator("//a[contains(text(), 'Мои студенты')]").is_hidden()

    @allure.step("Проверяем видимость кнопки 'Мои студенты'")
    def my_students_button_is_visible(self):
        my_students_btn = self.page.wait_for_selector(
            "//a[contains(text(), 'Мои студенты')]", state="visible"
        )
        return my_students_btn.is_visible()

    @allure.step("Кликаем на кнопку 'Мои студенты'")
    def click_my_students_btn(self):
        my_students_btn = self.page.wait_for_selector(
            "//a[contains(text(), 'Мои студенты')]", state="visible"
        )
        my_students_btn.click()
        url = self.page.url
        return url

    @allure.step("Кликаем кнопку 'Мое объявление'")
    def click_my_announcement_button(self):
        self.page.locator("a", has_text="Мое объявление").click()
        expect(self.page).to_have_url(
            "http://testing.misleplav.ru/listings/my_listing/"
        )

    @allure.step("Наводим мышку на кнопку 'Войти' и проверяем изменение цвета")
    def hover_login_button_color_check(self):
        button = self.page.locator(
            '(//a[@class="btn btn-outline-light mb-2 me-2 ms-3"])[1]'
        )
        original_color = button.evaluate(
            "el => window.getComputedStyle(el).backgroundColor"
        )
        button.hover()

        expect(button).not_to_have_css("background-color", original_color)

    @allure.step("Кнопка 'Мыслеплав' расположена в хедере")
    def header_home_btn_is_present(self):
        # Locate the home button in the header
        header_home_btn = self.page.locator('//a[@data-testid="logo"]')

        return header_home_btn

    @allure.step("Проверяем наличие кнопки 'Выйти' в профиле студента")
    def check_exit_btn_exists_for_student(self):
        exit_button = self.page.get_by_role("link", name="Выйти")
        return exit_button.is_visible()

    @allure.step("Кликаем кнопку 'Выйти' в профиле студента")
    def click_exit_btn_for_student(self):
        button = self.page.locator("a", has_text="Выйти")
        button.click()
        expect(self.page).to_have_url("http://testing.misleplav.ru/")

    @allure.step("Наводим мышку на кнопку 'Выйти' и проверяем изменение цвета")
    def hover_exit_button_for_student_color_check(self):
        exit_button = self.page.locator("a", has_text="Выйти")
        original_color = exit_button.evaluate(
            "el => window.getComputedStyle(el).backgroundColor"
        )
        exit_button.hover()
        hovered_color = exit_button.evaluate(
            "el => window.getComputedStyle(el).backgroundColor"
        )
        assert original_color != (
            hovered_color,
            f"Цвет кнопки 'Выйти' не изменился при наведении. Исходный: {original_color}, после наведения: {hovered_color}",
        )

    @allure.step("Наводим курсор на кнопку 'Профиль' и проверяем изменение ее цвета")
    def hover_profile_btn_color_check(self):
        button = self.page.locator("//a[@data-testid='profile']")
        original_color = button.evaluate("el => getComputedStyle(el).backgroundColor")
        button.hover()
        expect(button).not_to_have_css("background-color", original_color)
