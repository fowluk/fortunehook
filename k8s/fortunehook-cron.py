apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: fortunehook
  namespace: utils
spec:
  schedule: "*/15 * * * *"
  jobTemplate:
    metadata:
      name: fortunehook
      namespace: utils
    spec:
      template:
        spec:
         containers: 
           - name: fortunehook
             image: fowluk/fortunehook
             imagePullPolicy: Always
             envFrom:
               - secretRef:
                   name: fortunehookids
         restartPolicy: Never
         imagePullSecrets:
           - name: fowluk
