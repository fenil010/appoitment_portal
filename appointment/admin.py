from django.contrib import admin
from .models import Doctor, Appointment, Profile, Notification, StatusHistory, DoctorSchedule, TimeBlock, AppointmentReminder, Review, PatientNotes


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'patient_name',
        'doctor',
        'appointment_date',
        'appointment_time',
        'status',
        'priority',
    )
    list_filter = ('status', 'priority', 'doctor', 'appointment_date')
    search_fields = ('patient_name', 'patient_email', 'reason')
    readonly_fields = ('created_at', 'updated_at')
    raw_id_fields = ('user', 'doctor')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'specialization',
        'email',
        'is_active',
    )
    list_filter = ('specialization', 'is_active')
    search_fields = ('name', 'email', 'specialization')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'role',
        'phone',
        'email_notifications',
    )
    list_filter = ('role', 'email_notifications')
    search_fields = ('user__username', 'user__email')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'type',
        'title',
        'is_read',
        'created_at',
    )
    list_filter = ('type', 'is_read')
    search_fields = ('user__username', 'title', 'message')
    raw_id_fields = ('user', 'appointment')


@admin.register(StatusHistory)
class StatusHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'appointment',
        'old_status',
        'new_status',
        'changed_by',
        'changed_at',
    )
    list_filter = ('old_status', 'new_status')
    search_fields = ('appointment__patient_name',)
    raw_id_fields = ('appointment', 'changed_by')


@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'doctor',
        'day_of_week',
        'start_time',
        'end_time',
        'is_available',
    )
    list_filter = ('day_of_week', 'is_available')
    raw_id_fields = ('doctor',)


@admin.register(TimeBlock)
class TimeBlockAdmin(admin.ModelAdmin):
    list_display = (
        'doctor',
        'start_datetime',
        'end_datetime',
        'reason',
    )
    list_filter = ('doctor',)
    raw_id_fields = ('doctor',)


@admin.register(AppointmentReminder)
class AppointmentReminderAdmin(admin.ModelAdmin):
    list_display = (
        'appointment',
        'reminder_type',
        'hours_before',
        'is_sent',
        'scheduled_for',
    )
    list_filter = ('reminder_type', 'is_sent')
    raw_id_fields = ('appointment',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'doctor',
        'patient',
        'rating',
        'is_approved',
        'created_at',
    )
    list_filter = ('is_approved', 'rating')
    search_fields = ('doctor__name', 'patient__username')
    raw_id_fields = ('doctor', 'patient', 'appointment')


@admin.register(PatientNotes)
class PatientNotesAdmin(admin.ModelAdmin):
    list_display = (
        'appointment',
        'doctor',
        'created_at',
    )
    list_filter = ('doctor',)
    raw_id_fields = ('appointment', 'doctor')
