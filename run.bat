@ECHO OFF

SET WORKSPACE_PATH=%~f1
SET IMAGE_PATH=%~f2

colmap automatic_reconstructor --workspace_path %WORKSPACE_PATH% --image_path %IMAGE_PATH%
