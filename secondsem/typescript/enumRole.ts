enum UserRole {
    Admin,
    Editor,
    Viewer
}

function describeRole(role: UserRole): void {
    switch (role) {
        case UserRole.Admin:
            console.log("You have full access.");
            break;
        case UserRole.Editor:
            console.log("You can edit content.");
            break;
        case UserRole.Viewer:
            console.log("You can view content.");
            break;
    }
}

describeRole(UserRole.Editor); // Output: You can edit content.
