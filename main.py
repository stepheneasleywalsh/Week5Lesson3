# Create function to look up error codes
def errorCode(num):
    match num:
        case 401:
            return "You don't have authorisation"
        case 403:
            return "You don't have permission"
        case 404:
            return "Page not found"
        case 408:
            return "Timeout error, process stoped by user"
        case 500:
            return "Internal page not found"
        case 502:
            return "Connection problem"
        case 503:
            return "Website offline"
        case 504:
            return "Timeout error, no response from server"
        case other:
            return "Sorry, I don't know that code"

# Test it
print(errorCode(404))

quit()
