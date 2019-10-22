export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface FarmProfile {
    id: number;
    time_updated?: string;
    time_created?: string;
    farm_name: string;
    url: string;
    username: string;
    notes?: string;
    tags?: string;
}

export interface FarmProfileUpdate {
    farm_name?: string;
    url?: string;
    username?: string;
    password?: string;
    notes?: string;
    tags?: string;
}

export interface FarmProfileCreate {
    farm_name: string;
    url: string;
    username: string;
    password: string;
    notes?: string;
    tags?: string;
}
