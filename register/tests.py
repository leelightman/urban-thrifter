from django.test import TestCase
from .models import HelpseekerProfile, DonorProfile
from .forms import HelpseekerForm, DonorForm, HelpseekerUpdateForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from crispy_forms.helper import FormHelper


class EmailTests(TestCase):
    def test_email_sent(self):
        holder = self.client.get(reverse("register:email-sent"))
        self.assertEqual(holder.status_code, 200)
        self.assertContains(holder, "Confirmation email has been sent!")

    def test_change_password(self):
        user = User.objects.create(
            username="test",
            email="ponathanjun@gmail.com",
            password="peaches12",
        )
        holder = self.client.post(
            "/register/activate/"
            + urlsafe_base64_encode(force_bytes(user.pk))
            + "/"
            + PasswordResetTokenGenerator().make_token(user),
            {"password1": "peaches14", "password2": "peaches14"},
        )
        self.assertEqual(holder.status_code, 200)


class RegisterPageViewTests(TestCase):
    def test_register_redirect(self):
        holder = self.client.get(reverse("register:register"))
        self.assertEqual(holder.status_code, 200)
        self.assertContains(holder, "Are you a _______?")


class HelpseekerRegistrationTests(TestCase):
    def test_username_label(self):
        form = HelpseekerForm()
        self.assertTrue(form.fields["username"].label == "")

    def test_email_label(self):
        form = HelpseekerForm()
        self.assertTrue(form.fields["email"].label == "")

    def test_password_label(self):
        form = HelpseekerForm()
        self.assertTrue(form.fields["password1"].label == "")

    def test_password2_label(self):
        form = HelpseekerForm()
        self.assertTrue(form.fields["password2"].label == "")

    def test_borough_label(self):
        form = HelpseekerForm()
        self.assertTrue(form.fields["borough"].label == "Borough")

    def test_resource_label(self):
        form = HelpseekerForm()
        self.assertTrue(form.fields["resource"].label == "")

    def test_form_working(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_username_wrong(self):
        form = HelpseekerForm(
            data={
                "username": "jon",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_email_wrong(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_password_wrong(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "dog",
                "password2": "dog",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_password_match_wrong(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches13",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_resource_wrong(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["dogs", "cats"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_username_missing(self):
        form = HelpseekerForm(
            data={
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_email_missing(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_password1_missing(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_password2_missing(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_borough_missing(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_username_taken(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        form.save()
        duplicate = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "jonathanpun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(duplicate.is_valid())

    def test_email_taken(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        form.save()
        duplicate = HelpseekerForm(
            data={
                "username": "Brian",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        self.assertFalse(duplicate.is_valid())


class HelpseekerProfileTests(TestCase):
    def test_helpseeker_profile_borough(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        form.save()
        user = User.objects.filter(id="1").first()
        profile = HelpseekerProfile(user=user)
        profile.borough = form.cleaned_data.get("borough")
        self.assertTrue(profile.borough == "MAN")

    def test_helpseeker_profile_resource(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE", "OTHERS"],
            }
        )
        form.save()
        user = User.objects.filter(id="1").first()
        profile = HelpseekerProfile(user=user)
        resources = form.cleaned_data.get("resource")
        d = {}
        for i in range(0, 3):
            if 0 <= i < len(resources):
                d["resource{0}".format(i)] = resources[i]
            else:
                d["resource{0}".format(i)] = None
        profile.rc_1 = d["resource0"]
        profile.rc_2 = d["resource1"]
        profile.rc_3 = d["resource2"]
        self.assertTrue(
            profile.rc_1 == "FOOD"
            and profile.rc_2 == "MEDICAL/ PPE"
            and profile.rc_3 == "OTHERS"
        )

    def test_helpseeker_profile_complaint_count(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        form.save()
        user = User.objects.filter(id="1").first()
        profile = HelpseekerProfile(user=user)
        self.assertTrue(profile.complaint_count == 0)

    def test_helpseeker_str(self):
        form = HelpseekerForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            }
        )
        form.save()
        user = User.objects.filter(id="1").first()
        profile = HelpseekerProfile(user=user)
        self.assertEquals(
            "%s" % (profile.user),
            profile.__str__(),
        )


class HelpseekerViewTests(TestCase):
    def test_successful_post_request(self):
        holder = self.client.post(
            reverse("register:helpseeker-register"),
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            },
        )
        self.assertEqual(holder.status_code, 302)
        # self.assertEqual(holder["Location"], "/register/email-sent")

    def test_bad_username_post_request(self):
        holder = self.client.post(
            reverse("register:helpseeker-register"),
            data={
                "username": "jon",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            },
        )
        self.assertEqual(holder.status_code, 200)
        # self.assertContains(holder, "Help Seeker Registration")

    def test_bad_email_post_request(self):
        holder = self.client.post(
            reverse("register:helpseeker-register"),
            data={
                "username": "Jonathan",
                "email": "ponathanjun",
                "password1": "peaches12",
                "password2": "peaches12",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            },
        )
        self.assertEqual(holder.status_code, 200)
        # self.assertContains(holder, "Help Seeker Registration")

    def test_bad_password_post_request(self):
        holder = self.client.post(
            reverse("register:helpseeker-register"),
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "dog",
                "password2": "dog",
                "borough": "MAN",
                "resource": ["FOOD", "MEDICAL/ PPE"],
            },
        )
        self.assertEqual(holder.status_code, 200)
        # self.assertContains(holder, "Help Seeker Registration")

    def test_helpseeker_register_get(self):
        holder = self.client.get(reverse("register:helpseeker-register"))
        self.assertEqual(holder.status_code, 200)
        # self.assertContains(holder, "Help Seeker Registration")


class DonorRegistrationTests(TestCase):
    def test_username_label(self):
        form = DonorForm()
        self.assertTrue(form.fields["username"].label == "")

    def test_email_label(self):
        form = DonorForm()
        self.assertTrue(form.fields["email"].label == "")

    def test_password_label(self):
        form = DonorForm()
        self.assertTrue(form.fields["password1"].label == "")

    def test_password2_label(self):
        form = DonorForm()
        self.assertTrue(form.fields["password2"].label == "")

    def test_form_working(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_username_wrong(self):
        form = DonorForm(
            data={
                "username": "jon",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_email_wrong(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_password_wrong(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "dog",
                "password2": "dog",
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_password_match_wrong(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches13",
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_username_missing(self):
        form = DonorForm(
            data={
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_email_missing(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_password1_missing(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password2": "peaches12",
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_password2_missing(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
            }
        )
        self.assertFalse(form.is_valid())

    def test_username_taken(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        form.save()
        duplicate = DonorForm(
            data={
                "username": "Jonathan",
                "email": "jonathanpun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        self.assertFalse(duplicate.is_valid())

    def test_email_taken(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        form.save()
        duplicate = DonorForm(
            data={
                "username": "Brian",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        self.assertFalse(duplicate.is_valid())


class DonorProfileTests(TestCase):
    def test_donor_profile_donation_count(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        form.save()
        user = User.objects.filter(id="1").first()
        profile = DonorProfile(user=user)
        self.assertTrue(profile.donation_count == 0)

    def test_donor_profile_complaint_count(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        form.save()
        user = User.objects.filter(id="1").first()
        profile = DonorProfile(user=user)
        self.assertTrue(profile.complaint_count == 0)

    def test_donor_str(self):
        form = DonorForm(
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            }
        )
        form.save()
        user = User.objects.filter(id="1").first()
        profile = DonorProfile(user=user)
        self.assertEquals(
            "%s" % (profile.user),
            profile.__str__(),
        )


class DonorViewTests(TestCase):
    def test_successful_post_request(self):
        holder = self.client.post(
            reverse("register:donor-register"),
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            },
        )
        self.assertEqual(holder.status_code, 302)
        self.assertEqual(holder["Location"], "/register/email-sent")

    def test_bad_username_post_request(self):
        holder = self.client.post(
            reverse("register:donor-register"),
            data={
                "username": "jon",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches12",
            },
        )
        self.assertEqual(holder.status_code, 200)
        # self.assertContains(holder, "Donor Registration")

    def test_bad_email_post_request(self):
        holder = self.client.post(
            reverse("register:donor-register"),
            data={
                "username": "Jonathan",
                "email": "ponathanjun",
                "password1": "peaches12",
                "password2": "peaches12",
            },
        )
        self.assertEqual(holder.status_code, 200)
        # self.assertContains(holder, "Donor Registration")

    def test_bad_password_post_request(self):
        holder = self.client.post(
            reverse("register:donor-register"),
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "dog",
                "password2": "dog",
            },
        )
        self.assertEqual(holder.status_code, 200)
        # self.assertContains(holder, "Donor Registration")

    def test_mismatch_password_post_request(self):
        holder = self.client.post(
            reverse("register:donor-register"),
            data={
                "username": "Jonathan",
                "email": "ponathanjun@gmail.com",
                "password1": "peaches12",
                "password2": "peaches13",
            },
        )
        self.assertEqual(holder.status_code, 200)
        # self.assertContains(holder, "Donor Registration")

    def test_helpseeker_register_get(self):
        holder = self.client.get(reverse("register:donor-register"))
        self.assertEqual(holder.status_code, 200)
        # self.assertContains(holder, "Donor Registration")

    def test_helpseeker_register_home(self):
        holder = self.client.get(reverse("register:register"))
        self.assertEqual(holder.status_code, 200)


class UserDeleteTests(TestCase):
    def test_delete_user(self):
        user = User.objects.create(
            username="test",
            email="rahulgarg0697@gmail.com",
            password="Nyu2020!",
        )
        uname = user.username
        user.delete()
        length = len(User.objects.filter(username=uname))

        self.assertEqual(length, 0)


class ErrorTests(TestCase):
    def test_serve_error(self):
        holder = self.client.get("register/errorpage/500_server_error.html")
        holder.status_code = 500
        self.assertEqual(holder.status_code, 500)

    def test_bad_gate_day(self):
        holder = self.client.get("register/errorpage/502_bad_gateway.html")
        holder.status_code = 500
        self.assertEqual(holder.status_code, 500)

    def test_error(self):
        holder = self.client.get("register/errorpage/error.html")
        self.assertEqual(holder.status_code, 404)

    def test_page_not_found(self):
        holder = self.client.get("register/errorpage/404_page_not_found.html")
        self.assertEqual(holder.status_code, 404)

    def test_permission_denied(self):
        holder = self.client.get("register/errorpage/403_permission_denied.html")
        holder.status_code = 403
        self.assertEqual(holder.status_code, 403)

    def helpseeker_update_form(self):
        updateform = HelpseekerUpdateForm()
        self.assertEquals(updateform.helper.form_show_labels, False)

    def helpseeker_update_form_2(self):
        updateform = HelpseekerUpdateForm()
        self.assertEquals(updateform.helper, FormHelper(updateform))
