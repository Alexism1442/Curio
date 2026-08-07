# Curio release R8 rules.
#
# R8 is enabled for production releases. Keep the field names and model
# members used by Gson's reflective backup/capture serialization; otherwise
# obfuscation can make an exported backup unreadable by a later app version.
# Keep the data model package narrow so the rest of the app still benefits
# from shrinking and obfuscation.

# Gson may deserialize classes without invoking Kotlin constructors and reads
# fields reflectively. Preserve model names and fields in the data package.
-keep class com.curio.app.data.CaptureData { *; }
-keep class com.curio.app.data.CaptureData$* { *; }
-keep class com.curio.app.data.CaptureEntity { *; }
-keep class com.curio.app.data.BackupPayload { *; }
-keep class com.curio.app.data.PrefEntry { *; }
-keep class com.curio.app.data.FieldMindMetadata { *; }
-keep class com.curio.app.data.FieldMindSpecies { *; }
-keep enum com.curio.app.data.CaptureFormat { *; }
-keep enum com.curio.app.data.NotePaperStyle { *; }
-keep enum com.curio.app.data.NotePaperColor { *; }
-keep enum com.curio.app.data.JournalMood { *; }

# Preserve Gson's generic signatures and annotations used by reflective model
# parsing. R8 still shrinks unrelated implementation code.
-keepattributes Signature
-keepattributes *Annotation*

# Room's generated implementation and schema annotations are resolved through
# generated code/annotations; retain annotations but do not keep the entire
# application package.
-keep class com.curio.app.data.CurioDatabase { *; }
-keep class com.curio.app.data.CurioDatabase_Impl { *; }
-keep @androidx.room.Database class * { *; }
