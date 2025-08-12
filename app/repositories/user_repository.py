from app.SupabaseConnection import supabase_connection


class UserRepository:
    @staticmethod
    def get_users(limit: int = None) -> list[dict[str, str]]:
        try:
            response = (
                supabase_connection.client.table("user")
                .select("*")
                .limit(limit)
                .execute()
            )
            return response.data
        except Exception as e:
            print(e)

    @staticmethod
    def get_user_by_email(user_email: str) -> dict[str, str] | None:
        try:
            response = (
                supabase_connection.client.table("user")
                .select("*")
                .eq("email", user_email)
                .single()
                .execute()
            )
            return response.data
        except Exception as e:
            print(e)