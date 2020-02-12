apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: fortunehook
  namespace: utils
spec:
  schedule: "30 8 * * *"
  jobTemplate:
    metadata:
      name: fortunehook
      namespace: utils
    spec:
      template:
        spec:
         containers: 
           - name: fortunehook
             image: "fowluk/fortunehook:v1.1"
             envFrom:
               - secretRef:
                   name: fortunehookids
         restartPolicy: Never
