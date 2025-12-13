export function EnvironmentInfo() {
  return (
    <div className="pt-4 text-xs text-muted-foreground border-t">
      <p>Environment: {process.env.NEXT_PUBLIC_APP_ENV}</p>
      <p>Firebase Project: {process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID}</p>
      <p>Port: 3000</p>
    </div>
  );
}
