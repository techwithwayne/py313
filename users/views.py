# Import necessary modules from Django
from django.shortcuts import render, redirect  # Used to render HTML templates and redirect users
from django.contrib import messages  # Used to display one-time messages to users (e.g., success or error messages)
from django.contrib.auth.decorators import login_required  # Restricts access to views to authenticated users
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm  # Import custom forms from the current app

# View function for user registration
def register(request):
    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Create an instance of the registration form populated with POST data
        form = UserRegisterForm(request.POST)
        # Validate the form data
        if form.is_valid():
            # Save the new user to the database
            form.save()
            # Retrieve the cleaned username from the form data
            username = form.cleaned_data.get('username')
            # Display a success message to the user
            messages.success(request, f'Your account has been created! You are now able to log in')
            # Redirect the user to the login page after successful registration
            return redirect('login')
    else:
        # If the request is not POST, create an empty registration form
        form = UserRegisterForm()
    # Render the registration template with the form instance
    return render(request, 'users/register.html', {'form': form})

# View function for displaying and updating user profile
@login_required  # Ensures that only authenticated users can access this view
def profile(request):
    # Create instances of the user update form and profile update form
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    
    # Store the form instances in a context dictionary
    context = {
        'u_form': u_form,  # User update form
        'p_rom': p_form   # Profile update form (Note: Possible typo here, should it be 'p_form'?)
    }
    # Render the profile template with the context data
    return render(request, 'users/profile.html', context)
